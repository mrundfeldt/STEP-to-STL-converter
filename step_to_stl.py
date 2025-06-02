import sys
import os
import FreeCAD
import Part
import Mesh
import sys

print("Arguments received:", sys.argv)

def process_step_file(step_path):
    stl_path = os.path.splitext(step_path)[0] + ".stl"
    print(f"\nProcessing: {step_path}")
    try:
        shape = Part.read(step_path)
        if shape.isNull():
            print("Shape is empty.")
            return
        doc = FreeCAD.newDocument()
        part_obj = doc.addObject("Part::Feature", "ImportedPart")
        part_obj.Shape = shape
        Mesh.export([part_obj], stl_path)
        print(f"Exported to: {stl_path}")
    except Exception as e:
        print(f"Error: {e}")

def find_step_files(path):
    if os.path.isdir(path):
        # Search folder for STEP files
        return [
            os.path.join(path, f)
            for f in os.listdir(path)
            if f.lower().endswith(('.step', '.stp'))
        ]
    elif os.path.isfile(path) and path.lower().endswith(('.step', '.stp')):
        return [path]
    else:
        return []

# Entry point
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Drag STEP file(s) or a folder onto the .bat file to convert them.")
        sys.exit(1)

    for arg in sys.argv[1:]:
        step_files = find_step_files(arg)
        if not step_files:
            print(f"No STEP files found in: {arg}")
        for step_file in step_files:
            process_step_file(step_file)
