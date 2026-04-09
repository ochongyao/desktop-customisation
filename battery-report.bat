@echo off
REM Get the directory where the batch file is located
set "batchDir=%~dp0"

REM Generate battery report in the same directory as the batch file
powercfg /batteryreport /output "%batchDir%battery-report.html"

REM Open the report in default browser
start "" "%batchDir%battery-report.html"

REM Wait for user to close the browser
pause

REM Delete the report
del "%batchDir%battery-report.html"