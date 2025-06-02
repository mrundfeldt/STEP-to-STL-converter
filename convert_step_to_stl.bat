@echo off
REM Change to the directory where this .bat file lives
cd /d "%~dp0"

REM Run the Python script using FreeCAD's headless interpreter
"C:\Users\rundfeldt_m1\AppData\Local\Programs\FreeCAD 1.0\bin\python.exe" "step_to_stl.py" %*

REM Pause so the console stays open to view messages
REM pause