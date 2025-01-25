# Dataset

## Getting started
```bash
python -m venv .venv --prompt dataset-env
source .venv/bin/activate
pip install -r requirements.txt
```

## Schema checker
Use this file to verify that the schema files are correct.
```bash
python schema_checker.py
```


## Checker
Use this file to go over all directories, and check that all entries in the dataset conform to the required schemas.
```bash
python checker.py
```
