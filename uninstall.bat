@echo off
chcp 65001 >nul
title Alexandria Uninstaller

net session >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Please right-click this file and select "Run as administrator".
    pause
    exit /b
)

echo [*] Stopping Alexandria...
taskkill /f /im alexandria.exe >nul 2>&1

echo [*] Removing Run Key...
reg delete HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v AlexandriaMonitor /f >nul 2>&1

echo [*] Removing Scheduled Task...
schtasks /Delete /TN "AlexandriaTask" /F >nul 2>&1

echo [*] Removing Defender exclusion...
powershell -Command "Remove-MpPreference -ExclusionPath '%APPDATA%\Alexandria'" 2>nul

echo [*] Removing files...
rmdir /S /Q "%APPDATA%\Alexandria" 2>nul

echo.
echo [OK] Alexandria completely removed.
pause