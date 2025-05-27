This project is a small python-based STEP to STL converter based on https://github.com/tpaviot/pythonocc-core

It was born out of the need to transform STEP files from CAD systems into STL files for 3d-printing slicers. This is now largely unneccessary, as modern slicers parse STEPs internally.

I'm still putting it on here to keep myself accountable for my work and learn more about making code usable for other people than myself - especially regarding documentation.

Preparation: install the needed library (bash)
pip install pythonocc-core

Usage: (bash)
python step_to_stl.py model.step model.stl


