"""Headless-Chrome measurements for a fixture: axe violations, horizontal overflow, screenshots.

Chrome is driven through --dump-dom on a small wrapper page that loads the target in an
iframe, injects axe-core into it, and writes the result into the wrapper's DOM.
"""
import json
import pathlib
import re
import subprocess
import tempfile

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
AXE = pathlib.Path(__file__).parent / "node_modules" / "axe-core" / "axe.min.js"

WRAPPER = """<!doctype html><html><body style="margin:0"><pre id="out">pending</pre>
<iframe id="f" src="{src}" style="position:absolute;left:0;top:0;width:{width}px;height:900px;border:0"></iframe>
<script>
const f = document.getElementById('f'), out = document.getElementById('out');
f.onload = () => {{
  const d = f.contentDocument, w = f.contentWindow;
  const s = d.createElement('script'); s.src = '{axe}';
  s.onload = () => w.axe.run(d, {{ runOnly: ['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22aa','best-practice'] }}).then(r => {{
    out.textContent = JSON.stringify({{
      scrollWidth: d.documentElement.scrollWidth,
      bg: w.getComputedStyle(d.body).backgroundColor,
      violations: r.violations.map(v => ({{ id: v.id, impact: v.impact, nodes: v.nodes.length }}))
    }});
  }});
  d.head.appendChild(s);
}};
</script></body></html>"""


def _chrome(args):
    return subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                           "--allow-file-access-from-files", *args],
                          capture_output=True, text=True, timeout=60)


def measure(html_path, width=1280, dark=False):
    html_path = pathlib.Path(html_path).resolve()
    wrapper = WRAPPER.format(src=html_path.as_uri(), axe=AXE.resolve().as_uri(), width=width)
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as t:
        t.write(wrapper)
    args = ["--virtual-time-budget=5000", "--dump-dom"]
    if dark:
        args.insert(0, "--force-dark-mode")
    r = _chrome(args + [pathlib.Path(t.name).as_uri()])
    m = re.search(r'<pre id="out">(.*?)</pre>', r.stdout, re.S)
    if not m or m.group(1) == "pending":
        return {"error": "no result", "stderr": r.stderr[-300:]}
    return json.loads(m.group(1).replace("&quot;", '"').replace("&amp;", "&"))


SHIFT = """<!doctype html><html><body style="margin:0"><pre id="out">pending</pre>
<iframe id="f" src="__SRC__" style="position:absolute;left:0;top:0;width:__WIDTH__px;height:900px;border:0"></iframe>
<script>
const f = document.getElementById('f'), out = document.getElementById('out');
const CLICK = __CLICK__;
f.onload = () => {
  const d = f.contentDocument;
  const snap = () => new Map(Array.from(d.body.querySelectorAll('*')).map(e => { const r = e.getBoundingClientRect(); return [e, [r.top, r.left]]; }));
  const moved = (a, b, skip) => { let n = 0, max = 0;
    b.forEach((v, e) => { const u = a.get(e); if (!u || (skip && skip.contains(e))) return;
      const dy = Math.abs(v[0] - u[0]), dx = Math.abs(v[1] - u[1]);
      if (dy > 0.5 || dx > 0.5) { n++; max = Math.max(max, dy, dx); } });
    return { n, max: Math.round(max) }; };
  const a = snap();
  setTimeout(() => {
    const b = snap(), settle = moved(a, b);
    let click = { n: 0, max: 0 };
    if (CLICK) { const c = d.querySelector(CLICK); if (c) { c.click(); setTimeout(() => {
      click = moved(b, snap(), c); out.textContent = JSON.stringify({ settle, click }); }, 300); return; } }
    out.textContent = JSON.stringify({ settle, click });
  }, 1500);
};
</script></body></html>"""


def shift(html_path, click=None, width=390):
    """Count elements whose top/left move after load settles and after clicking `click`."""
    html_path = pathlib.Path(html_path).resolve()
    wrapper = (SHIFT.replace("__SRC__", html_path.as_uri()).replace("__WIDTH__", str(width))
               .replace("__CLICK__", json.dumps(click)))
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as t:
        t.write(wrapper)
    r = _chrome(["--virtual-time-budget=6000", "--dump-dom", pathlib.Path(t.name).as_uri()])
    m = re.search(r'<pre id="out">(.*?)</pre>', r.stdout, re.S)
    if not m or m.group(1) == "pending":
        return {"error": "no result", "stderr": r.stderr[-300:]}
    return json.loads(m.group(1).replace("&quot;", '"').replace("&amp;", "&"))


def screenshot(html_path, out_png, width=1280, height=900, dark=False):
    args = [f"--window-size={width},{height}", f"--screenshot={out_png}"]
    if dark:
        args.insert(0, "--force-dark-mode")
    _chrome(args + [pathlib.Path(html_path).resolve().as_uri()])
