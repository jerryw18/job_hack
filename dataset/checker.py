import os
from utils import list_directories, load_json, validate_json_files

def main():
    workspace = os.getcwd()
    directories = list_directories(workspace)
    
    for directory in directories:
        print(f"Checking directory: {directory}")
        schema_path = os.path.join(workspace, directory, 'schema.json')
        if os.path.exists(schema_path):
            schema = load_json(schema_path)
            validate_json_files(os.path.join(workspace, directory), schema)
        else:
            print(f"No schema.json found in {directory}")

if __name__ == "__main__":
    main()
