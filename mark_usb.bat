@echo off
chcp 65001 >nul
title Alexandria v3 - USB Marker Tool

echo ================================================================
echo   Alexandria v3 - USB Marker Tool
echo ================================================================
echo.
echo This tool will create a marker file on the USB drive.
echo Only USBs with this marker can trigger auto-export.
echo.
echo Target drive: %~d0
echo.
pause

set DRIVE=%~d0
set MARKER=%DRIVE%\ALEXANDRIA.md

echo.
echo [*] Creating marker file: %MARKER%

> "%MARKER%" echo ALEXANDRIA-AUTHORIZED-EXPORT-KEY-v3-2026

if exist "%MARKER%" (
    echo.
    echo [OK] Marker file created successfully.
    echo.
    echo File contents:
    type "%MARKER%"
) else (
    echo.
    echo [!] Failed to create marker file.
    echo [!] Make sure the USB is not write-protected.
    pause
    exit /b
)

echo.
echo ================================================================
echo   USB marked as Alexandria v3 target
echo ================================================================
echo.
echo The USB will now trigger auto-export when plugged into
echo any system where Alexandria v3 is running.
echo.
pause