from jsonschema import validate, ValidationError

# Schema for action item JSON objects
ACTION_ITEM_SCHEMA = {
    "type": "object",
    "properties": {
        "task": {"type": "string"},
        "owner": {"type": ["string", "null"]},
        "due_date": {"type": ["string", "null"]}
    },
    "required": ["task", "owner", "due_date"]
}

# Validate a single action item JSON object
def is_valid_action_item(item):
    try:
        validate(instance=item, schema=ACTION_ITEM_SCHEMA)
        return True
    except ValidationError:
        return False
