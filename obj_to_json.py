import sys
import json

def obj_to_json(obj_file, json_file):
    vertices = []
    faces = []

    with open(obj_file, 'r') as file:
        for line in file:
            if line.startswith('v '):
                parts = line.strip().split()
                vertices.append([float(parts[1]), float(parts[2]), float(parts[3])])
            elif line.startswith('f '):
                parts = line.strip().split()
                face = [int(part.split('/')[0]) - 1 for part in parts[1:]]
                faces.append(face)

    output = {
        "vertices": vertices,
        "faces": faces
    }

    with open(json_file, 'w') as file:
        json.dump(output, file)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("❗ Usage: python obj_to_json.py input.obj output.json")
    else:
        obj_file = sys.argv[1]
        json_file = sys.argv[2]
        obj_to_json(obj_file, json_file)
        print(f"✅ Converted '{obj_file}' to '{json_file}'")
