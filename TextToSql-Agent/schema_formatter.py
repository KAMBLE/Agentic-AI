import json
import os

def format_schema():

    file_path = os.path.join(os.path.dirname(__file__), "schema_description.json")
    with open(file_path) as f:
        schema = json.load(f)

    lines = ["Schema:"]
    for table, meta in schema.items():
        lines.append(f"TABLE {table}: {meta.get('description', '')}")
        for col, desc in meta["columns"].items():
            lines.append(f"  - {col}: {desc}")
        lines.append("")
    return "\n".join(lines).strip()
