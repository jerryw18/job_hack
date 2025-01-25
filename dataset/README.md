# Dataset
This is the dataset folder that can be uses for prototyping.

## Getting started
```bash
python -m venv .venv --prompt dataset-env
source .venv/bin/activate
pip install -r requirements.txt
```

When restarting work in a fresh shell you can activate the virtual environment via:
```bash
source .venv/bin/activate
```

## Running the checkers
There are two checkers in this area:
* `schema_checker`: Checks that all the schemas are valid.
* `checker`: Checks each entry on every directory conforms to the expected schema.

### Schema checker
Use this file to verify that the schema files are correct.
```bash
python schema_checker.py
```

### Checker
Use this file to go over all directories, and check that all entries in the dataset conform to the required schemas.
```bash
python checker.py
```
