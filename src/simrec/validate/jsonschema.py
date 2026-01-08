# simrec/validate/jsonschema.py
# Eugene Joseph M. Ragasa
# - initial validator: 1/8/2026

import json
from importlib.resources import files
from typing import Any

from jsonschema import Draft202012Validator


def load_schema(name: str) -> dict[str, Any]:
  path = files("simrec.schema").joinpath(name)
  return json.loads(path.read_text(encoding="utf-8"))


def validator_for(name: str) -> Draft202012Validator:
  schema = load_schema(name)
  return Draft202012Validator(schema)


def validate_instance(name: str, instance: dict[str, Any]) -> None:
  v = validator_for(name)
  errors = sorted(v.iter_errors(instance), key=lambda e: e.path)
  if errors:
    msg = "\n".join([f"{list(e.path)}: {e.message}" for e in errors])
    raise ValueError(f"Schema validation failed for {name}:\n{msg}")

