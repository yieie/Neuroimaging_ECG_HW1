"""
polar_bridge.py — 讓 PsychoPy 自動在 WebPolarReader 插入 marker

用法：
    python polar_bridge.py VerityCollectionToolv0.057.html

然後用 Chrome / Edge 打開 http://localhost:8765/
（不要直接雙擊 html 檔，要從這個網址開，marker 才會連動）

PsychoPy 每次呼叫 http://localhost:8765/marker?label=XXX，
網頁就會自動插入一個名為 XXX 的 marker（等同手動點 marker 按鈕）。

只用 Python 標準函式庫，不需要安裝任何套件。
"""
import json
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

PORT = 8765

# 注入到 WebPolarReader 網頁裡的程式：每 100 ms 問一次有沒有新的 marker
INJECT = """
<script>
(function () {
  var box = document.createElement('div');
  box.id = 'bridge_status';
  box.style.cssText = 'position:fixed;right:8px;bottom:8px;padding:6px 10px;'
    + 'font:13px sans-serif;background:#fde68a;border:1px solid #b45309;z-index:9999';
  box.textContent = 'PsychoPy bridge: 連線中…';
  document.body.appendChild(box);
  var count = 0;
  setInterval(function () {
    fetch('/poll').then(function (r) { return r.json(); }).then(function (labels) {
      box.style.background = '#bbf7d0';
      labels.forEach(function (label) {
        InsertMarker(label);            // WebPolarReader 原本的 marker 函式
        count += 1;
        box.textContent = 'PsychoPy bridge: 已連線｜marker ' + count + '：' + label;
      });
      if (count === 0) box.textContent = 'PsychoPy bridge: 已連線，等待 marker';
    }).catch(function () {
      box.style.background = '#fecaca';
      box.textContent = 'PsychoPy bridge: 斷線！請確認 polar_bridge.py 還在執行';
    });
  }, 100);
})();
</script>
"""

queue = []
lock = threading.Lock()


def load_page(html_path):
    html = Path(html_path).read_text(encoding="utf-8")
    idx = html.lower().rfind("</html>")
    return (html[:idx] + INJECT + html[idx:]) if idx != -1 else html + INJECT


class Handler(BaseHTTPRequestHandler):
    def _send(self, body, ctype="application/json"):
        data = body.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", ctype + "; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        url = urlparse(self.path)
        if url.path == "/":
            self._send(load_page(self.server.html_path), "text/html")
        elif url.path == "/marker":
            label = parse_qs(url.query).get("label", ["marker"])[0]
            with lock:
                queue.append(label)
            print(time.strftime("%H:%M:%S"), "marker:", label, flush=True)
            self._send('{"ok": true}')
        elif url.path == "/poll":
            with lock:
                items = queue[:]
                queue.clear()
            self._send(json.dumps(items, ensure_ascii=False))
        else:
            self.send_error(404)

    def log_message(self, *args):  # 不印每一次 poll
        pass


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("用法：python polar_bridge.py VerityCollectionToolv0.057.html")
    server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    server.html_path = sys.argv[1]
    print(f"Bridge 已啟動：請用 Chrome 打開 http://localhost:{PORT}/")
    print("按 Ctrl+C 結束")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
