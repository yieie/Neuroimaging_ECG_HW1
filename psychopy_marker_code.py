# ================================================================
# 貼到 PsychoPy Builder 的 Code component（Code Type 選 Py）
# ================================================================

# ---------- Begin Experiment 分頁（放在第一個 routine 的 Code component）----------
import threading
import time
import urllib.parse
import urllib.request

def send_marker(label):
    """送 marker 到 WebPolarReader，並把精確時間存進 PsychoPy 的 csv。
    用背景執行緒送出，不會卡住畫面。"""
    t = time.time()                       # 系統時間（秒），與 marker 的毫秒時間同一個時鐘
    thisExp.addData(label + '_epoch', t)  # PsychoPy csv 也留一份精確時間
    full = f"{label}|{t:.3f}"             # marker 名稱附上 PsychoPy 的時間，方便事後核對
    url = "http://localhost:8765/marker?label=" + urllib.parse.quote(full)
    def _go():
        try:
            urllib.request.urlopen(url, timeout=1)
        except Exception as e:
            print("marker 送出失敗：", label, e)
    threading.Thread(target=_go, daemon=True).start()


# ---------- 每個 routine 各自的 Code component ----------
# 以吹氣球的 routine 為例（其他 routine 把名稱換掉即可）：

# Begin Routine 分頁：
send_marker("balloon_start")

# End Routine 分頁：
send_marker("balloon_end")

# 建議的名稱：
#   sync（開場「準備開始」畫面）、baseline_start / baseline_end、
#   slowbreath_start / slowbreath_end、balloon_start / balloon_end、
#   rest_start / rest_end、rating_start / rating_end、post_end
# 名稱請用英文、不要有空白。
