import sys
import os
import FreeCAD
import Part
import Mesh

def ask_for_step_file():
    print("Please enter the path to a STEP file:")
    step_path = input(">>> ").strip('"').strip("'")
    if not os.path.isfile(step_path):
        print("File not found.")
        sys.exit(1)
    return step_path

# Ask user for file path
step_path = ask_for_step_file()

# Build output path
stl_path = os.path.splitext(step_path)[0] + ".stl"

print(f"Reading STEP file: {step_path}")
try:
    shape = Part.read(step_path)
except Exception as e:
    print(f"Error reading STEP file: {e}")
    sys.exit(1)

if shape.isNull():
    print("Error: Shape is empty.")
    sys.exit(1)

print("Creating FreeCAD document and object...")
doc = FreeCAD.newDocument()
part_obj = doc.addObject("Part::Feature", "ImportedPart")
part_obj.Shape = shape

print(f"Exporting STL to: {stl_path}")
try:
    Mesh.export([part_obj], stl_path)
    print("Export successful!")
except Exception as e:
    print(f"Error exporting STL: {e}")
    sys.exit(1)
