# tests/validate/schemas/test_validator_for.py
# Eugene Joseph M. Ragasa

# --- function being tested
from simrec.validate.jsonschema import validator_for

def test_event_schema_loads():
  validator_for("event.schema.json")

def test_claim_schema_loads():
  validator_for("claim.schema.json")

