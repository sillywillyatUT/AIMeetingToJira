import json

def merge_json_arrays(json_strings):
    """
    Merge multiple JSON arrays into one.
    Deduplicates by task string.
    """
    merged = []
    seen = set()

    for js in json_strings:
        try:
            items = json.loads(js)
            for item in items:
                task = item.get("task")
                if task and task not in seen:
                    merged.append(item)
                    seen.add(task)
        except json.JSONDecodeError:
            print("Skipping invalid JSON chunk")

    return merged
