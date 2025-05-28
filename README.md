This project is a small python-based STEP to STL converter that was supposed to be based on https://github.com/tpaviot/pythonocc-core

It was born out of the need to transform STEP files from CAD systems into STL files for 3d-printing slicers. This is now largely unneccessary, as modern slicers parse STEPs internally.

I'm still putting it on here to keep myself accountable for my work and learn more about making code usable for other people than myself - especially regarding documentation.

---------------------------------

Getting pythonocc to run on my work machine inside a restricted environment was impossible due to the network connections needed by Anaconda. Therefore, a workaround was needed and found within FreeCAD.

To use the script, first install FreeCAD, which brings its own python environment and cmd shell: https://www.freecad.org/downloads.php

The script is then run from PowerShell with the following command:

& "C:\Users\$USER\AppData\Local\Programs\FreeCAD 1.0\bin\FreeCADCmd.exe" "C:\Python\step_to_stl.py"

The file path needs to be entered in PowerShell when prompted, and the script will return an STL with the same name in the original folder.
