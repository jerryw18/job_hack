import os
import json
import jsonschema
from jsonschema import validate

def list_directories(workspace):
    listdirs =[d for d in os.listdir(workspace) if os.path.isdir(os.path.join(workspace, d))]
    listdirs.remove('.venv')
    listdirs.remove('__pycache__')
    return listdirs

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def validate_json_files(directory, schema):
    for file_name in os.listdir(directory):
        if file_name.endswith('.json') and file_name != 'schema.json':
            file_path = os.path.join(directory, file_name)
            try:
                data = load_json(file_path)
                validate(instance=data, schema=schema)
                print(f"{file_name} is valid.")
            except jsonschema.exceptions.ValidationError as err:
                print(f"{file_name} is invalid: {err}")
            except Exception as e:
                print(f"Error processing {file_name}: {e}")
