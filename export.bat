@echo off
chcp 65001 >nul
title Alexandria v2 Export

if not exist "%APPDATA%\Alexandria\alexandria.exe" (
    echo [!] Alexandria is not installed on this system.
    pause
    exit /b
)

echo [*] Checking if target is a USB drive...
set DRIVETYPE=Unknown
for /f "tokens=3" %%A in ('fsutil fsinfo drivetype %~d0 2^>nul') do set DRIVETYPE=%%A

if /i not "%DRIVETYPE%"=="Removable" (
    echo [!] ERROR: This is NOT a removable USB drive.
    echo [!] Detected drive type: %DRIVETYPE%
    pause
    exit /b
)

echo [*] USB drive detected. Exporting Alexandria v2 logs...
"%APPDATA%\Alexandria\alexandria.exe" --export "%~dp0."

echo.
echo [OK] Logs exported to: %~dp0logs_export
echo [OK] HTML report: %~dp0logs_export\report.html
echo [OK] ZIP archive: %~dp0alexandria_export.zip
pause