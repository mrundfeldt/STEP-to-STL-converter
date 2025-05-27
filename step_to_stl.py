import sys
from OCC.Core.STEPControl import STEPControl_Reader
from OCC.Core.StlAPI import StlAPI_Writer
from OCC.Core.BRepMesh import BRepMesh_IncrementalMesh
from OCC.Core.TopExp import TopExp_Explorer
from OCC.Core.TopAbs import TopAbs_FACE
from OCC.Core.BRep import BRep_Tool

def step_to_stl(step_file: str, stl_file: str, linear_deflection: float = 0.1, angular_deflection: float = 0.5):
    # Load the STEP file
    step_reader = STEPControl_Reader()
    status = step_reader.ReadFile(step_file)
    if status != 0:
        raise Exception("Error reading STEP file.")

    step_reader.TransferRoots()
    shape = step_reader.OneShape()

    # Mesh the shape for STL export
    mesh = BRepMesh_IncrementalMesh(shape, linear_deflection, False, angular_deflection, True)
    mesh.Perform()

    # Export to STL
    stl_writer = StlAPI_Writer()
    stl_writer.SetASCIIMode(False)
    success = stl_writer.Write(shape, stl_file)

    if not success:
        raise Exception("Error writing STL file.")

    print(f"Successfully converted '{step_file}' to '{stl_file}'.")

# Example usage:
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python step_to_stl.py input.step output.stl")
        sys.exit(1)
    step_to_stl(sys.argv[1], sys.argv[2])
