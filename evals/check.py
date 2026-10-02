"""Score an edited fixture against its original.

    python3 evals/check.py <fixture> <edited-index.html>

Reports: visible-text preservation, pattern/structural checks, axe violations (light/dark, 1280/320),
and horizontal overflow at 320px. Pattern hits are a screen, not a verdict: read the flagged output.
"""
import difflib
import json
import pathlib
import re
import sys
from html.parser import HTMLParser

import browser

HERE = pathlib.Path(__file__).parent
INTERACTIVE = {"button", "a", "input", "select", "textarea", "label", "summary", "option"}


class Scan(HTMLParser):
    """Collects visible strings, input/label wiring, and onclick usage."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.texts, self.skip = [], 0
        self.inputs, self.label_for, self.in_label = [], set(), 0
        self.clickables, self.aria_labels, self.imgs = [], [], []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "style"):
            self.skip += 1
        if tag == "label":
            self.in_label += 1
            if a.get("for"):
                self.label_for.add(a["for"])
        if tag in ("input", "select", "textarea") and a.get("type", "text") not in ("hidden", "submit", "button", "image"):
            self.inputs.append((tag, a.get("id"), bool(self.in_label)))
        if tag == "input" and a.get("type", "text") in ("text", "email", "password", "search") and a.get("value"):
            self.texts.append(a["value"])
        if tag == "img":
            self.imgs.append(a)
        for k in ("placeholder", "alt"):
            if a.get(k):
                self.texts.append(a[k])
        if a.get("aria-label"):
            self.aria_labels.append(a["aria-label"])
        if "onclick" in a and tag not in INTERACTIVE:
            self.clickables.append((tag, a.get("role"), a.get("tabindex")))

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip -= 1
        if tag == "label":
            self.in_label -= 1

    def handle_data(self, data):
        if not self.skip and data.strip():
            self.texts.append(data)


def norm(s):
    return re.sub(r"\s+", " ", s).strip().lower()


def scan(path):
    s = Scan()
    s.feed(pathlib.Path(path).read_text())
    return s


def structural(name, s, html=""):
    if name == "imgs_sized":
        has_ratio = bool(re.search(r"aspect-ratio", html, re.I))
        bad = [i for i in s.imgs if not ((i.get("width") and i.get("height")) or has_ratio)]
        return not bad, f"{len(bad)} of {len(s.imgs)} images lack width+height attributes and the page has no aspect-ratio"
    if name == "inputs_labelled":
        bad = [i for i in s.inputs if not (i[2] or (i[1] and i[1] in s.label_for))]
        return not bad, f"{len(bad)} of {len(s.inputs)} inputs lack an associated <label>"
    if name == "no_clickable_non_interactive":
        bad = [c for c in s.clickables if not (c[1] and c[2] is not None)]
        return not bad, f"{len(bad)} non-interactive elements with onclick and no role+tabindex"
    raise ValueError(name)


def pattern_check(html, c, want_match):
    html = re.sub(r"/\*.*?\*/|<!--.*?-->", "", html, flags=re.S)
    pats = c.get("patterns") or [c["pattern"]]
    hit = any(re.search(p, html, re.I | re.S) for p in pats)
    if "unless" in c and re.search(c["unless"], html, re.I | re.S):
        hit = False
    return hit if want_match else not hit


def axe_summary(path):
    rows = {}
    for dark in (False, True):
        for width in (1280, 320):
            r = browser.measure(path, width, dark)
            key = f"{'dark ' if dark else 'light'} {width}"
            if "error" in r:
                rows[key] = (None, None, r["error"])
                continue
            rows[key] = (sum(v["nodes"] for v in r["violations"]), r["scrollWidth"],
                         ", ".join(f"{v['id']}x{v['nodes']}" for v in r["violations"]))
    return rows


def main(fixture, edited):
    orig_path = HERE / "fixtures" / fixture / "index.html"
    checks = json.loads((HERE / "fixtures" / fixture / "checks.json").read_text())
    html = pathlib.Path(edited).read_text()
    so, se = scan(orig_path), scan(edited)

    new_blob = norm(" ".join(se.texts))
    old_blob = norm(" ".join(so.texts))
    removed = sorted({norm(t) for t in so.texts if norm(t) not in new_blob})
    added = sorted({norm(t) for t in se.texts if norm(t) not in old_blob})
    print(f"## {fixture}: {edited}")
    print(f"\nContent: {len(removed)} original strings missing, {len(added)} new visible strings")
    for t in removed:
        print(f"  - MISSING  {t!r}")
    for t in added:
        print(f"  + ADDED    {t!r}")
    if se.aria_labels:
        print(f"  (non-visible aria-labels: {se.aria_labels})")

    diff = [l for l in difflib.unified_diff(orig_path.read_text().splitlines(), html.splitlines(), lineterm="", n=0)
            if l[:1] in "+-" and l[:3] not in ("+++", "---")]
    print(f"\nDiff size: {len(diff)} changed lines (originally {len(orig_path.read_text().splitlines())} lines)")

    print("\nPattern checks")
    fails = 0
    for c in checks["must_match"]:
        ok = pattern_check(html, c, True)
        fails += not ok
        print(f"  {'PASS' if ok else 'FAIL'}  {c['id']:<24} {c['note']}")
    for c in checks["must_not_match"]:
        ok = pattern_check(html, c, False)
        fails += not ok
        print(f"  {'PASS' if ok else 'FAIL'}  {c['id']:<24} (must be gone) {c['note']}")
    for name in checks["structural"]:
        ok, msg = structural(name, se, html)
        fails += not ok
        print(f"  {'PASS' if ok else 'FAIL'}  {name:<24} {msg}")
    orig_dir, edited_dir = orig_path.parent, pathlib.Path(edited).parent
    for rel in checks.get("unchanged", []):
        ok = (edited_dir / rel).exists() and (edited_dir / rel).read_bytes() == (orig_dir / rel).read_bytes()
        fails += not ok
        print(f"  {'PASS' if ok else 'FAIL'}  unchanged:{rel:<15} shared file must not be edited")
    if "unchanged" in checks:
        skip = ("shots/", "REPORT.md")
        orig_files = {str(p.relative_to(orig_dir)) for p in orig_dir.rglob("*") if p.is_file()}
        added = sorted(str(p.relative_to(edited_dir)) for p in edited_dir.rglob("*")
                       if p.is_file() and not str(p.relative_to(edited_dir)).startswith(skip)
                       and str(p.relative_to(edited_dir)) not in orig_files)
        ok = not added
        fails += not ok
        print(f"  {'PASS' if ok else 'FAIL'}  new-files              {added or 'none created'}")
    if "shift" in checks:
        sh = browser.shift(edited, checks["shift"].get("click"), checks["shift"].get("width", 390))
        if "error" in sh:
            print(f"  FAIL  layout-shift           measurement failed: {sh['error']}")
            fails += 1
        else:
            for phase, label in (("settle", "after load settles"), ("click", "after clicking the control")):
                ok = sh[phase]["n"] == 0
                fails += not ok
                print(f"  {'PASS' if ok else 'FAIL'}  shift:{phase:<17} {sh[phase]['n']} elements moved (max {sh[phase]['max']}px) {label}")
    print(f"  => {fails} failed")

    print("\nBrowser (axe violating nodes | scrollWidth)   original -> edited")
    before, after = axe_summary(orig_path), axe_summary(edited)
    for k in before:
        b, a = before[k], after[k]
        print(f"  {k:<11} axe {b[0]} -> {a[0]}   scrollWidth {b[1]} -> {a[1]}")
        print(f"              remaining: {a[2] or 'none'}")
    if checks.get("manual"):
        print("\nManual review")
        for m in checks["manual"]:
            print(f"  [ ] {m}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
