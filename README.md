<div align="center">

<h1>⚡ Alexandria</h1>

<p><strong>Monitor the system. Capture the activity. Prove the integrity.</strong></p>
<p>A bilingual, laboratory-grade activity monitor for authorized cybersecurity education — from keystrokes and clipboard to process launches and HTML forensics dashboards.</p>

<a href="#-english"><img src="https://img.shields.io/badge/READ%20IN%20ENGLISH-5ee7ff?style=for-the-badge&logo=readthedocs&logoColor=07111f" alt="Read in English"></a>
<a href="#-فارسی"><img src="https://img.shields.io/badge/خواندن%20به%20فارسی-ff6bd6?style=for-the-badge&logo=bookstack&logoColor=ffffff" alt="Read in Persian"></a>

</div>

[![Platform](https://img.shields.io/badge/Platform-Windows%2010%20%7C%2011-0078D6?style=for-the-badge&logo=windows&logoColor=white)](https://www.microsoft.com/windows)
[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.13-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)
[![Lab Only](https://img.shields.io/badge/Use-Authorized%20Laboratory%20Only-red?style=for-the-badge)]()

[![HTML](https://img.shields.io/badge/Report-HTML%20Dashboard-orange?style=flat-square)](#)
[![SHA-256](https://img.shields.io/badge/Integrity-SHA--256-green?style=flat-square)](#)
[![ZIP](https://img.shields.io/badge/Export-ZIP%20Compressed-blue?style=flat-square)](#)
[![Single Instance](https://img.shields.io/badge/Single--Instance-Mutex%20Protected-purple?style=flat-square)](#)

> A bilingual, laboratory-grade activity monitoring tool for authorized cybersecurity training — capturing 9 log types with professional HTML reporting.

<div align="center">

| 🎯 9 Log Types | 🌍 2 Languages | 🧠 MITRE Mapped | 🔐 Integrity Verified |
|:---:|:---:|:---:|:---:|
| `keyboard · window · browser · clipboard · process · usb · system · activity` | `EN + FA` | `7 Techniques` | `SHA-256` |

</div>

<details>
<summary><strong>🎬 Open the quick-start briefing</strong></summary>

```text
┌──────────────────────────────────────────────────────────────────────┐
│   INSTALL  →  RUN SILENTLY  →  COLLECT  →  EXPORT  →  ANALYZE       │
│      ↓             ↓              ↓           ↓           ↓          │
│   install.bat   persistence   9 log types   ZIP+HTML   report.html   │
│                  (Run Key +    thread-safe  SHA-256    MITRE map     │
│                   Task)        rotation     ZIP        insights      │
└──────────────────────────────────────────────────────────────────────┘
```

</details>

## Table of Contents

- [About](#about)
- [Why Alexandria?](#why-alexandria)
- [Who Is This For?](#who-is-this-for)
- [What You'll Learn](#what-youll-learn)
- [Project Stats](#project-stats)
- [How to Use This Project](#how-to-use-this-project)
- [Prerequisites](#prerequisites)
- [Features Overview](#features-overview)
- [Technologies and Tools](#technologies-and-tools)
- [Repository Structure](#repository-structure)
- [Deployment Workflow](#deployment-workflow)
- [Key Security Concepts](#key-security-concepts)
- [MITRE ATT&CK Mapping](#mitre-attck-mapping)
- [Sample Output](#sample-output)
- [Roadmap](#roadmap)
- [FAQ](#faq)
- [Related Resources](#related-resources)
- [Version History](#version-history)
- [Contributing](#contributing)
- [Disclaimer](#disclaimer)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Author](#author)

## About

**Alexandria** is a laboratory-grade activity monitoring tool designed for **authorized cybersecurity training**. It runs silently on Windows systems, capturing a comprehensive picture of user and system activity — then produces a professional HTML report with SHA-256 integrity verification and a compressed ZIP archive for easy transfer.

Named after the legendary **Library of Alexandria** — the ancient world's greatest repository of knowledge — this tool embodies the same principle: **gather, preserve, and present information with integrity**.

Every log entry, every process launch, every clipboard event is captured with millisecond precision and stored in a thread-safe, rotation-aware log system.

## Why Alexandria?

Most keyloggers are single-purpose toys. Most EDR tools are enterprise-heavy monoliths. Alexandria sits in between: **a teaching-grade monitoring tool** that demonstrates professional techniques without the enterprise overhead.

It was built for a cybersecurity laboratory course, with emphasis on:

- **Real-world techniques** — Persistence via Registry + Scheduled Task
- **Data integrity** — SHA-256 manifest for every log file
- **Professional reporting** — GitHub-dark HTML dashboard
- **Bilingual support** — Persian and English keyboard layouts
- **Defensive awareness** — Every feature maps to a defensive lesson

## Who Is This For?

- **Cybersecurity students** learning monitoring fundamentals
- **Instructors** teaching digital forensics and endpoint detection
- **Pentesters** building understanding of persistence mechanisms
- **Blue teamers** studying what EDR tools capture
- **Researchers** needing a controlled data-collection baseline
- **Anyone** with written authorization to monitor a specific system

## What You'll Learn

- Implement Windows persistence (Registry Run Key + Scheduled Task)
- Build a thread-safe, multi-feature logging system in Python
- Capture keyboard input across layouts (Persian + English) with VK codes
- Extract browser history from SQLite databases in real-time
- Monitor clipboard, processes, USB events, and idle state
- Generate SHA-256 integrity manifests for forensic evidence
- Build a dark-mode HTML dashboard with pure CSS
- Compress forensic data with ZIP for evidence preservation
- Apply MITRE ATT&CK framework to a real tool
- Understand defensive countermeasures for each technique

## Project Stats

| Metric | Value |
|---|---|
| Log types | 9 (keylog, activity, browser, clipboard, process, usb, system, + reports) |
| Languages | English and Persian |
| Platform | Windows 10 / 11 |
| Persistence methods | 2 (Run Key + Scheduled Task) |
| Integrity | SHA-256 manifest per file |
| Report format | HTML dashboard + ZIP archive |
| Config | JSON (12 options) |
| Single-instance | Windows Mutex |
| Author | Leo / Ilya Farahani |

## How to Use This Project

1. **Read the Disclaimer carefully** — this tool requires written authorization.
2. **Get written permission** from the system owner and your instructor.
3. **Review the source code** (`alexandria.py`) before deployment.
4. **Test on your own machine first** using the provided scripts.
5. **Deploy on the authorized target** via `install.bat` (Run as admin).
6. **Wait the monitoring period** — no USB needed during this time.
7. **Export evidence** with `export.bat` on the final day.
8. **Analyze** `report.html` and raw logs.
9. **Uninstall cleanly** with `uninstall.bat` after evaluation.

## Prerequisites

**Required:**
- Windows 10 or Windows 11 (x64)
- Administrator access on the target system
- Python 3.10+ (for building from source)
- Written authorization for the target system

**Recommended:**
- Basic Python knowledge
- Familiarity with Windows Registry
- Understanding of Windows Task Scheduler
- A modern browser (for viewing `report.html`)

## Features Overview

| # | Feature | Description | Config Key |
|---|---------|-------------|------------|
| 1 | ⌨️ **Keyboard Logger** | CHAR (native) + EN (physical) + VK (virtual key code) | always on |
| 2 | 🪟 **Active Window Monitor** | Process name + window title on every focus change | always on |
| 3 | 🌐 **Browser History Extractor** | Chrome + Edge SQLite history every 5 minutes | `browser_extract_interval` |
| 4 | 📋 **Clipboard Monitor** | Captures every clipboard change with 500-char preview | `enable_clipboard` |
| 5 | ⚙️ **Process Launch Monitor** | Records every newly launched process with PID + user | `enable_process_monitor` |
| 6 | 💤 **Idle Detection** | Filters out keystrokes during user inactivity | `enable_idle_detection` |
| 7 | 🔌 **USB Event Monitor** | Tracks removable drive connect/disconnect | `enable_usb_events` |
| 8 | 🖥️ **System Info Collector** | Hostname, OS, CPU, RAM, user every 6 hours | `system_info_interval` |
| 9 | 📊 **HTML Report Generator** | Dark-mode dashboard with stats and bar charts | `enable_html_report` |

| Bonus Feature | Purpose |
|---------------|---------|
| 🔄 **Log Rotation** | Splits files when they exceed `log_max_size_mb` |
| 🔐 **SHA-256 Manifest** | Cryptographic proof of file integrity |
| 📦 **ZIP Export** | Compresses all logs on export |
| 🛡️ **Single-Instance Mutex** | Prevents duplicate processes |
| ⚙️ **JSON Config** | Change behavior without recompiling |

## Technologies and Tools

| Category | Technologies |
|---|---|
| **Language** | Python 3.10–3.13 |
| **Keyboard Capture** | `pynput` (cross-layout listener) |
| **Process/System** | `psutil` |
| **Windows APIs** | `win32gui`, `win32process`, `win32clipboard`, `ctypes` |
| **Database** | `sqlite3` (browser history extraction) |
| **Packaging** | PyInstaller (`--onefile --noconsole`) |
| **Integrity** | `hashlib` (SHA-256) |
| **Compression** | `zipfile` (DEFLATE) |
| **Reporting** | Pure HTML + CSS (no JS framework) |
| **Persistence** | Registry Run Key + Task Scheduler |

| Tool | Purpose |
|---|---|
| CMD / PowerShell | Deployment and diagnostics |
| File Explorer | USB preparation and log inspection |
| Any Browser | Opening `report.html` |
| `certutil` / `sha256sum` | Verifying SHA-256 manifest |
| Windows Task Scheduler | Reviewing persistence |

## Repository Structure

```text
alexandria/
├── alexandria.py              # Main daemon + export module
├── alexandria.exe             # Compiled executable
├── config.json                # Runtime configuration
├── install.bat                # Day-1 installer
├── export.bat                 # Day-7 log exporter
├── uninstall.bat              # Post-project cleanup
├── README.md                  # This file
├── commands.txt               # Command reference card
├── LICENSE                    # MIT License
├── build/                     # PyInstaller temporary files
├── dist/                      # PyInstaller output
└── assets/                    # Images and diagrams (optional)
```

**Runtime layout on target system:**

```text
%APPDATA%\Alexandria\
├── alexandria.exe
└── logs\
    ├── keylog_YYYYMMDD.txt
    ├── activity_YYYYMMDD.txt
    ├── browser_YYYYMMDD.txt
    ├── clipboard_YYYYMMDD.txt
    ├── process_YYYYMMDD.txt
    ├── usb_YYYYMMDD.txt
    └── system_YYYYMMDD.txt
```

## Deployment Workflow

```text
┌─────────────────────────────────────────────────────────────────┐
│  DAY 0 — PREPARATION                                            │
│  ├── Build: pyinstaller --noconsole --onefile alexandria.py    │
│  ├── Copy 7 files to USB root                                  │
│  └── Verify hashes match on clean system                       │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  DAY 1 — INSTALLATION (USB plug #1)                            │
│  ├── Right-click install.bat → Run as administrator            │
│  ├── Defenders exclusion added automatically                   │
│  ├── Run Key + Scheduled Task created                          │
│  └── USB removed — Alexandria runs silently                    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  DAYS 1–7 — SILENT OPERATION                                   │
│  ├── 9 log types collected continuously                        │
│  ├── Auto-resumes after reboot (persistence)                   │
│  ├── Survives user logoff / shutdown / Fast Startup            │
│  └── Log rotation prevents file bloat                          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  DAY 7 — EXPORT (USB plug #2)                                  │
│  ├── Double-click export.bat FROM the USB drive                │
│  ├── HTML report generated (report.html)                       │
│  ├── SHA-256 manifest created (_hashes.sha256)                 │
│  ├── ZIP archive produced (alexandria_export.zip)              │
│  └── USB removed with all evidence                             │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  POST-PROJECT — CLEANUP                                        │
│  ├── Right-click uninstall.bat → Run as administrator          │
│  ├── All traces removed (files, registry, tasks, exclusions)   │
│  └── System returned to original state                         │
└─────────────────────────────────────────────────────────────────┘
```

## Key Security Concepts

### 1. Persistence via Registry Run Key

**Why it matters:** The Registry Run Key is a classic persistence mechanism used by both legitimate software and malware.

**How Alexandria uses it:** `HKCU\Software\Microsoft\Windows\CurrentVersion\Run\AlexandriaMonitor` → `alexandria.exe`

**How to defend:** Monitor Run Key modifications via Sysmon Event ID 13 or Windows Defender ATP.

### 2. Persistence via Scheduled Task

**Why it matters:** Scheduled Tasks are more resilient than Run Keys because they survive Fast Startup.

**How Alexandria uses it:** `AlexandriaTask` with `ONLOGON` trigger and `LIMITED` privilege.

**How to defend:** Audit `schtasks /query /fo LIST /v` regularly; alert on unexpected ONLOGON tasks.

### 3. Single-Instance via Named Mutex

**Why it matters:** Duplicate processes cause duplicate logging, corrupted data, and resource exhaustion.

**How Alexandria uses it:** `Global\Alexandria_Lab_Monitor_Mutex_2026` with `ERROR_ALREADY_EXISTS` check.

**How to defend:** Named mutexes are legitimate; malware uses them to prevent multiple infections.

### 4. SHA-256 Integrity Manifest

**Why it matters:** Logs are worthless as evidence if they can be tampered with.

**How Alexandria uses it:** Every exported file gets a SHA-256 hash in `_hashes.sha256`.

**How to defend:** Always verify SHA-256 before accepting forensic evidence in court.

### 5. Clipboard Monitoring

**Why it matters:** Users copy passwords, tokens, and sensitive data to the clipboard without thinking.

**How Alexandria uses it:** `win32clipboard` polling every 3 seconds with 500-char preview.

**How to defend:** Use clipboard managers with auto-clear; disable clipboard history for sensitive apps.

### 6. Cross-Layout Keyboard Capture

**Why it matters:** A keylogger that only understands QWERTY misses Persian, Arabic, and other layouts.

**How Alexandria uses it:** Captures CHAR (native) + EN (from VK) + VK (raw code) for every key.

**How to defend:** Behavior-based detection instead of signature-based — pattern of fast, rhythmic input.

### 7. USB Device Event Tracking

**Why it matters:** Data exfiltration often happens via removable media.

**How Alexandria uses it:** `psutil.disk_partitions()` polled every 10 seconds for removable drives.

**How to defend:** Use Windows Defender Device Control or equivalent DLP policies.

## MITRE ATT&CK Mapping

| Technique | ID | Alexandria Feature | Defense |
|-----------|-----|-------------------|---------|
| Input Capture: Keylogging | **T1056.001** | Keyboard Logger | Behavior analytics, EDR |
| Clipboard Data | **T1115** | Clipboard Monitor | Clipboard restrictions |
| Screen Capture | **T1113** | (not implemented) | — |
| Registry Run Keys / Startup Folder | **T1547.001** | Run Key Persistence | Sysmon Event ID 13 |
| Scheduled Task / Job | **T1053.005** | Scheduled Task Persistence | Task Scheduler audit |
| Process Discovery | **T1057** | Process Monitor | Process creation auditing |
| System Information Discovery | **T1082** | System Info Collector | Baseline monitoring |
| File and Directory Discovery | **T1083** | Browser History Scan | Filesystem auditing |

> Alexandria demonstrates **7 techniques** across the **Discovery** and **Persistence** tactics. Every technique maps to a defensive control — this is the core educational value.

## Sample Output

### `keylog_20261007.txt`

```text
[2026-10-07 12:32:15] [chrome.exe] [Google - Search] CHAR: ن | EN: k | VK: 75
[2026-10-07 12:32:16] [chrome.exe] [Google - Search] CHAR: خ | EN: o | VK: 79
[2026-10-07 12:32:17] [chrome.exe] [Google - Search] CHAR: م | EN: l | VK: 76
[2026-10-07 12:32:18] [chrome.exe] [Google - Search] CHAR: <enter> | EN: <enter> | VK: 13
```

### `clipboard_20261007.txt`

```text
[2026-10-07 12:33:01] [chrome.exe] CLIP: https://example.com/login?token=abc123
[2026-10-07 12:34:15] [notepad.exe] CLIP: MySecretPassword2026!
```

### `process_20261007.txt`

```text
[2026-10-07 12:35:00] LAUNCH: chrome.exe | PID: 12345 | USER: LabUser | EXE: C:\Program Files\Google\Chrome\Application\chrome.exe
[2026-10-07 12:35:12] LAUNCH: notepad.exe | PID: 12346 | USER: LabUser | EXE: C:\Windows\System32\notepad.exe
```

### `report.html` (excerpt)

```html
<div class="card">
  <h2>Summary</h2>
  <div class="stat"><div class="num">133</div><div class="lbl">Keystrokes</div></div>
  <div class="stat"><div class="num">56</div><div class="lbl">Window Changes</div></div>
  <div class="stat"><div class="num">400</div><div class="lbl">Browser Visits</div></div>
  <div class="stat"><div class="num">8</div><div class="lbl">Clipboard Events</div></div>
  <div class="stat"><div class="num">148</div><div class="lbl">Process Launches</div></div>
</div>
```

## Roadmap

- [ ] Add screenshot capture with JPEG compression
- [ ] Add OCR-based screen content extraction
- [ ] Add network connection monitoring (established sockets)
- [ ] Add Windows Event Log integration (logon/logoff, privilege use)
- [ ] Add encrypted log storage (AES-256 via Fernet)
- [ ] Add remote retrieval via encrypted channel (opt-in)
- [ ] Add GUI viewer (`tkinter` or `PyQt`) for browsing logs offline
- [ ] Add Windows Service mode (System-level persistence)
- [ ] Add multi-language HTML report (EN + FA)
- [ ] Add signed EXE for reduced AV false positives
- [ ] Add automated test suite (`pytest`)
- [ ] Add GitHub Actions CI for releases

## FAQ

### Is Alexandria a keylogger?

Technically, yes — it captures keystrokes. But it's **far more**: it captures windows, processes, clipboard, browser history, USB events, and system info, then produces a professional report with integrity verification.

### Is this legal?

**Only with written authorization.** Deploying this on any system without explicit permission is illegal in most jurisdictions. This tool is designed for **authorized cybersecurity laboratory environments**.

### Why not just use commercial EDR?

Commercial EDR is closed-source and expensive. Alexandria is open, transparent, and educational — you can read every line of code and understand exactly what it does.

### Will antivirus flag `alexandria.exe`?

**Likely yes** on first run — PyInstaller binaries often trigger heuristic detection. The `install.bat` script automatically adds a Windows Defender exclusion. For other AV products, add the exclusion manually.

### How long does one deployment last?

The designed duration is **7 days**, but Alexandria is unbounded — it runs until uninstalled. The 7-day model just provides a clean deployment/export/cleanup cycle.

### Can I run this on Linux or macOS?

No — it relies on Windows-specific APIs (`win32gui`, `win32clipboard`, Registry, Task Scheduler).

### Can I modify it for my own course?

Yes, under the MIT License. Attribution is appreciated but not required.

### How do I verify the SHA-256 manifest?

On Windows PowerShell:

```powershell
Get-FileHash .\keylog_20261007.txt -Algorithm SHA256
```

Compare with the entry in `_hashes.sha256`.

## Related Resources

- [Sysinternals Sysmon](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon) — Microsoft's official system monitor
- [MITRE ATT&CK Framework](https://attack.mitre.org/) — adversary tactic knowledge base
- [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)
- [Windows Persistence Techniques](https://attack.mitre.org/tactics/TA0003/)
- [SANS Digital Forensics](https://www.sans.org/cyber-security-courses/digital-forensics-essentials/)
- [pynput Documentation](https://pynput.readthedocs.io/)
- [psutil Documentation](https://psutil.readthedocs.io/)
- [PyInstaller Manual](https://pyinstaller.org/)

## Version History

| Version | Date | Status | Highlights |
|---|---|---|---|
| **v2.0.0** | 2026-10-08 | Current | Clipboard, process, idle, USB, HTML report, SHA-256, ZIP |
| v1.0.0 | 2026-10-07 | Superseded | Initial release: keyboard, window, browser, system |
| v0.9.0 | 2026-10-06 | Archived | Beta: single-instance, persistence, export |
| v0.5.0 | 2026-10-05 | Archived | Prototype: keyboard capture only |

## Contributing

This project is primarily an educational artifact, but contributions are welcome for:

- **Bug fixes** — reproducible issues with clear steps
- **Documentation** — typos, clarifications, translations
- **Defensive ideas** — detection rules, countermeasures
- **Ethical improvements** — accessibility, transparency

Please open an issue before submitting a large pull request.

```bash
git checkout -b fix/meaningful-description
git add .
git commit -m "Describe the change and why"
git push origin fix/meaningful-description
```

## Disclaimer

**This tool is intended ONLY for authorized cybersecurity education and defensive research.**

By using Alexandria, you agree that:

1. You have **written authorization** from the system owner and your instructor.
2. You will deploy it **only** on the specifically authorized target system.
3. You will **destroy all collected data** after project evaluation.
4. You will **not** use it to harm, spy on, or surveil any individual without consent.
5. You understand that unauthorized use may violate **computer fraud laws** in your jurisdiction (e.g., CFAA in the US, Computer Misuse Act in the UK, Iran's Computer Crimes Law, and equivalents worldwide).

**The author and contributors assume no liability for misuse, damage, data loss, service interruption, or legal consequences arising from this material.**

Follow applicable laws, contracts, and organizational policies at all times.

## License

This project is distributed under the [MIT License](LICENSE).

Copyright © 2026 Leo (Ilya Farahani).

## Acknowledgments

- **Library of Alexandria** — for the inspiration behind the name
- **Microsoft Sysinternals** — for Sysmon, the gold standard of system monitoring
- **MITRE Corporation** — for the ATT&CK framework
- **pynput, psutil, PyInstaller teams** — for the excellent Python ecosystem
- **The cybersecurity community** — for sharing knowledge openly

## Author

**Leo (Ilya Farahani)**

- GitHub: [github.com/here-is-leo](https://github.com/here-is-leo)
- LinkedIn: [linkedin.com/in/ilya-farahani-2160103b0](https://www.linkedin.com/in/ilya-farahani-2160103b0)
- Telegram: [t.me/Here_is_leo](https://t.me/Here_is_leo)
- Email: [ilyafarahanii@gmail.com](mailto:ilyafarahanii@gmail.com)

---

<div align="center">
<h1 id="-فارسی">⚡ الکساندریا</h1>
<p><strong>سیستم را پایش کن. فعالیت را ثبت کن. یکپارچگی را اثبات کن.</strong></p>
<p>یک ابزار پایش فعالیت آزمایشگاهی، دوزبانه و حرفه‌ای، برای آموزش امنیت سایبری مجاز — از کیبورد و کلیپ‌بورد تا پایش پروسه‌ها و داشبورد HTML.</p>
</div>

## درباره پروژه

**الکساندریا** یک ابزار پایش فعالیت در سطح آزمایشگاهی است که برای **آموزش امنیت سایبری مجاز** طراحی شده. این ابزار به‌صورت بی‌صدا روی ویندوز اجرا می‌شود و تصویری جامع از فعالیت کاربر و سیستم ثبت می‌کند — سپس یک گزارش HTML حرفه‌ای با تأیید یکپارچگی SHA-256 و یک فایل ZIP فشرده تولید می‌کند.

نام این ابزار از **کتابخانه‌ی افسانه‌ای اسکندریه** — بزرگترین گنجینه‌ی دانش دنیای باستان — الهام گرفته شده. همان اصل: **جمع‌آوری، حفظ و ارائه‌ی اطلاعات با یکپارچگی**.

## چرا الکساندریا؟

بیشتر کی‌لاگرها اسباب‌بازی‌های تک‌منظوره‌اند. بیشتر ابزارهای EDR سنگین و سازمانی هستند. الکساندریا بین این دو می‌ایستد: **یک ابزار پایش در سطح آموزشی** که تکنیک‌های حرفه‌ای را بدون پیچیدگی سازمانی نشان می‌دهد.

## این پروژه برای چه کسانی است؟

- **دانشجویان امنیت سایبری** که مبانی پایش را یاد می‌گیرند
- **مدرسان** که جرم‌شناسی دیجیتال و شناسایی Endpoint را تدریس می‌کنند
- **تسترهای نفوذ** که می‌خواهند مکانیزم‌های پایداری را بفهمند
- **تیم‌های دفاعی (Blue Team)** که می‌خواهند بدانند EDRها چه چیزی را ثبت می‌کنند
- **پژوهشگران** که به یک پایه‌ی داده‌ی کنترل‌شده نیاز دارند
- **هر کسی** که **مجوز کتبی** برای پایش یک سیستم مشخص دارد

## چه چیزهایی یاد می‌گیرید؟

- پیاده‌سازی Persistence در ویندوز (Run Key + Scheduled Task)
- ساخت سیستم لاگ thread-safe و چندمنظوره در پایتون
- ثبت کیبورد در چند لی‌اوت (فارسی + انگلیسی) با کد VK
- استخراج تاریخچه‌ی مرورگر از SQLite به‌صورت real-time
- پایش کلیپ‌بورد، پروسه‌ها، رویدادهای USB و حالت Idle
- تولید مانیفست SHA-256 برای شواهد جرم‌شناسی
- ساخت داشبورد HTML دارک-مود با CSS خالص
- فشرده‌سازی داده‌های جرم‌شناسی در ZIP
- نگاشت تکنیک‌ها به فریمورک MITRE ATT&CK
- درک اقدامات دفاعی متناظر با هر تکنیک

## آمار پروژه

| شاخص | مقدار |
|---|---|
| انواع لاگ | ۹ (کیبورد، پنجره، مرورگر، کلیپ‌بورد، پروسه، USB، سیستم و گزارش‌ها) |
| زبان‌ها | انگلیسی و فارسی |
| پلتفرم | Windows 10 / 11 |
| روش‌های Persistence | ۲ (Run Key + Scheduled Task) |
| یکپارچگی | مانیفست SHA-256 برای هر فایل |
| قالب گزارش | داشبورد HTML + آرشیو ZIP |
| تنظیمات | JSON (۱۲ گزینه) |
| Single-instance | Windows Mutex |
| نویسنده | لئو / ایلیا فراهانی |

## نمای کلی قابلیت‌ها

| # | قابلیت | توضیح | کلید تنظیمات |
|---|---------|--------|---------------|
| ۱ | ⌨️ **کی‌لاگر** | CHAR (زبان مبدأ) + EN (فیزیکی) + VK (کد ویندوز) | همیشه فعال |
| ۲ | 🪟 **پایش پنجره فعال** | نام پروسه + عنوان پنجره در هر تغییر فوکوس | همیشه فعال |
| ۳ | 🌐 **استخراج تاریخچه مرورگر** | تاریخچه Chrome + Edge هر ۵ دقیقه | `browser_extract_interval` |
| ۴ | 📋 **پایش کلیپ‌بورد** | ثبت هر تغییر با پیش‌نمایش ۵۰۰ کاراکتری | `enable_clipboard` |
| ۵ | ⚙️ **پایش اجرای پروسه** | ثبت هر پروسه‌ی جدید با PID + کاربر | `enable_process_monitor` |
| ۶ | 💤 **تشخیص Idle** | فیلتر کیبورد در زمان بیکاری کاربر | `enable_idle_detection` |
| ۷ | 🔌 **پایش رویداد USB** | ردیابی اتصال/قطع درایوهای قابل جابجایی | `enable_usb_events` |
| ۸ | 🖥️ **جمع‌آوری اطلاعات سیستم** | Hostname، OS، CPU، RAM، کاربر هر ۶ ساعت | `system_info_interval` |
| ۹ | 📊 **تولید گزارش HTML** | داشبورد دارک-مود با آمار و نمودار میله‌ای | `enable_html_report` |

## جریان استقرار

```text
روز ۰ — آماده‌سازی
    └── ساخت EXE و کپی ۷ فایل روی فلش

روز ۱ — نصب (اتصال اول فلش)
    ├── راست‌کلیک install.bat → Run as administrator
    ├── Alexandria خودکار در پس‌زمینه اجرا می‌شود
    └── فلش جدا می‌شود — دیگر لازم نیست

روز ۱ تا ۷ — اجرای بی‌صدا
    ├── ۹ نوع لاگ به‌طور مداوم ثبت می‌شود
    ├── پس از هر ری‌استارت خودکار ادامه می‌یابد
    └── چرخش لاگ از فایل‌های غول جلوگیری می‌کند

روز ۷ — خروجی (اتصال دوم فلش)
    ├── دابل‌کلیک export.bat از روی فلش
    ├── گزارش HTML ساخته می‌شود
    ├── مانیفست SHA-256 تولید می‌شود
    └── فایل ZIP روی فلش قرار می‌گیرد

بعد از پروژه — پاک‌سازی
    ├── راست‌کلیک uninstall.bat → Run as administrator
    └── تمام ردپاها پاک می‌شوند
```

## مفاهیم کلیدی امنیتی

### ۱. Persistence از طریق Run Key رجیستری

**چرا مهم است:** Run Key یک مکانیزم کلاسیک Persistence است که هم نرم‌افزارهای قانونی و هم بدافزارها از آن استفاده می‌کنند.

**چگونه دفاع کنیم:** تغییرات Run Key را با Sysmon Event ID 13 پایش کنید.

### ۲. Persistence از طریق Scheduled Task

**چرا مهم است:** Taskها پایدارتر از Run Key هستند چون Fast Startup را تحمل می‌کنند.

**چگونه دفاع کنیم:** دستور `schtasks /query /fo LIST /v` را دوره‌ای اجرا کنید و روی Taskهای ONLOGON ناشناس هشدار بگذارید.

### ۳. یکپارچگی با مانیفست SHA-256

**چرا مهم است:** لاگ‌ها اگر قابل دستکاری باشند، به‌عنوان شواهد بی‌ارزش هستند.

**چگونه دفاع کنیم:** همیشه قبل از پذیرش شواهد در دادگاه، SHA-256 را بررسی کنید.

### ۴. پایش کلیپ‌بورد

**چرا مهم است:** کاربران رمز و توکن را بدون فکر کردن کپی می‌کنند.

**چگونه دفاع کنیم:** از clipboard manager با auto-clear استفاده کنید.

### ۵. ثبت کیبورد در چند لی‌اوت

**چرا مهم است:** کی‌لاگری که فقط QWERTY را می‌فهمد، فارسی و عربی و ... را از دست می‌دهد.

**چگونه دفاع کنیم:** تشخیص مبتنی بر رفتار به‌جای امضا.

## نگاشت MITRE ATT&CK

| تکنیک | شناسه | قابلیت الکساندریا | دفاع |
|--------|-------|-------------------|------|
| Input Capture: Keylogging | **T1056.001** | کی‌لاگر | تحلیل رفتاری، EDR |
| Clipboard Data | **T1115** | پایش کلیپ‌بورد | محدودسازی کلیپ‌بورد |
| Registry Run Keys | **T1547.001** | Persistence با Run Key | Sysmon Event ID 13 |
| Scheduled Task | **T1053.005** | Persistence با Task | حسابرسی Task Scheduler |
| Process Discovery | **T1057** | پایش پروسه | حسابرسی ساخت پروسه |
| System Info Discovery | **T1082** | جمع‌آوری اطلاعات سیستم | پایش baseline |
| File Discovery | **T1083** | اسکن تاریخچه مرورگر | حسابرسی فایل‌سیستم |

## سؤالات متداول

### آیا الکساندریا یک کی‌لاگر است؟

از نظر فنی بله — کیبورد را ثبت می‌کند. اما بسیار بیشتر از آن است: پنجره‌ها، پروسه‌ها، کلیپ‌بورد، تاریخچه مرورگر، رویدادهای USB و اطلاعات سیستم را هم ثبت می‌کند و یک گزارش حرفه‌ای با تأیید یکپارچگی تولید می‌کند.

### آیا این قانونی است؟

**فقط با مجوز کتبی.** استقرار این ابزار روی هر سیستمی بدون اجازه‌ی صریح در بیشتر کشورها غیرقانونی است. این ابزار برای **محیط آزمایشگاهی امنیت سایبری مجاز** طراحی شده.

### چرا از EDR تجاری استفاده نکنیم؟

EDR تجاری closed-source و گران است. الکساندریا باز، شفاف و آموزشی است — می‌توانی هر خط کد را بخوانی.

### آیا آنتی‌ویروس `alexandria.exe` را تشخیص می‌دهد؟

**احتمالاً بله** در اولین اجرا. اسکریپت `install.bat` خودکار پوشه را در Windows Defender استثنا می‌کند. برای سایر AVها، استثنا را دستی اضافه کن.

### آیا روی لینوکس یا مک اجرا می‌شود؟

خیر — به APIهای مخصوص ویندوز وابسته است.

### آیا برای دوره‌ی خودم می‌توانم تغییرش دهم؟

بله، تحت مجوز MIT. ذکر منبع قدردانی می‌شود ولی الزامی نیست.

## منابع مرتبط

- [Sysinternals Sysmon](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)
- [pynput Documentation](https://pynput.readthedocs.io/)
- [psutil Documentation](https://psutil.readthedocs.io/)
- [PyInstaller Manual](https://pyinstaller.org/)

## تاریخچه نسخه‌ها

| نسخه | تاریخ | وضعیت | ویژگی‌های کلیدی |
|---|---|---|---|
| **v2.0.0** | 2026-10-08 | فعلی | کلیپ‌بورد، پروسه، Idle، USB، گزارش HTML، SHA-256، ZIP |
| v1.0.0 | 2026-10-07 | جانشین‌شده | نسخه اولیه |
| v0.9.0 | 2026-10-06 | آرشیو | بتا: single-instance، persistence، export |
| v0.5.0 | 2026-10-05 | آرشیو | نمونه اولیه: فقط کیبورد |

## مشارکت

این پروژه عمدتاً یک اثر آموزشی است، اما مشارکت در این زمینه‌ها خوش‌آمد است:

- **رفع باگ** — با مراحل بازتولید واضح
- **مستندسازی** — غلط تایپی، شفاف‌سازی، ترجمه
- **ایده‌های دفاعی** — قواعد شناسایی، اقدامات متقابل
- **بهبودهای اخلاقی** — دسترس‌پذیری، شفافیت

## رفع مسئولیت

**این ابزار فقط برای آموزش امنیت سایبری مجاز و پژوهش دفاعی است.**

با استفاده از الکساندریا، شما تأیید می‌کنید:

۱. **مجوز کتبی** از مالک سیستم و استاد خود دارید.
۲. آن را **فقط** روی سیستم هدف مجاز مشخص‌شده مستقر می‌کنید.
۳. تمام داده‌های جمع‌آوری‌شده را بعد از ارزیابی پروژه **نابود می‌کنید**.
۴. از آن برای آسیب، جاسوسی یا نظارت بدون رضایت **استفاده نمی‌کنید**.
۵. می‌دانید که استفاده‌ی غیرمجاز ممکن است **قوانین جرایم رایانه‌ای** را در حوزه‌ی قضایی شما نقض کند.

**نویسنده و مشارکت‌کنندگان هیچ مسئولیتی در قبال سوءاستفاده، خسارت، از دست رفتن داده، اختلال سرویس یا پیامدهای قانونی ندارند.**

## مجوز

این پروژه تحت [مجوز MIT](LICENSE) منتشر شده است.

Copyright © 2026 Leo (Ilya Farahani).

## قدردانی

- **کتابخانه‌ی اسکندریه** — برای الهام‌بخش نام
- **Microsoft Sysinternals** — برای Sysmon
- **MITRE Corporation** — برای فریمورک ATT&CK
- **تیم‌های pynput، psutil، PyInstaller** — برای اکوسیستم پایتون
- **جامعه‌ی امنیت سایبری** — برای اشتراک‌گذاری دانش

## نویسنده

**لئو (ایلیا فراهانی)**

- گیت‌هاب: [github.com/here-is-leo](https://github.com/here-is-leo)
- لینکدین: [linkedin.com/in/ilya-farahani-2160103b0](https://www.linkedin.com/in/ilya-farahani-2160103b0)
- تلگرام: [t.me/Here_is_leo](https://t.me/Here_is_leo)
- ایمیل: [ilyafarahanii@gmail.com](mailto:ilyafarahanii@gmail.com)
