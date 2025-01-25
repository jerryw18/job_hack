import json
import jsonschema
from jsonschema import validate
from utils import list_directories
import os

def validate_and_print_schema(schema_file):
    print(f"Validating schema in {schema_file}")
    # Load the schema
    with open(schema_file, 'r') as file:
        schema = json.load(file)
    
    # Validate the schema
    try:
        validate(instance=schema, schema={"$ref": "http://json-schema.org/draft-07/schema#"})
        print("Schema is valid.")
    except jsonschema.exceptions.ValidationError as err:
        print("Schema is invalid:", err)
        return
    
    # Print the first level of fields
    print("First level fields in the schema:")
    for field in schema.get('properties', {}).keys():
        print(f"- {field}")


direcories = list_directories('.')
for dir in direcories:
    validate_and_print_schema(os.path.join(dir, 'schema.json'))
