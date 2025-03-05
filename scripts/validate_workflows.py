import json
import glob
import os
import sys

def validate():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_files = sorted(glob.glob(os.path.join(base_dir, "templates", "*", "*.json")))
    
    print(f"Validating {len(template_files)} workflow templates...")
    if len(template_files) != 62:
        print(f"Error: Expected 62 templates, found {len(template_files)}")
        sys.exit(1)
        
    errors = []
    for fpath in template_files:
        relpath = os.path.relpath(fpath, base_dir)
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            errors.append(f"{relpath}: JSON decode error: {e}")
            continue
            
        # Validate essential n8n workflow top-level fields
        for key in ["name", "nodes", "connections", "active", "settings"]:
            if key not in data:
                errors.append(f"{relpath}: Missing key '{key}'")
                
        node_names = set()
        for node in data.get("nodes", []):
            if "name" not in node or "type" not in node:
                errors.append(f"{relpath}: Node missing 'name' or 'type': {node}")
            else:
                node_names.add(node["name"])
                
        # Validate connections reference actual nodes
        for src, conn_map in data.get("connections", {}).items():
            if src not in node_names:
                errors.append(f"{relpath}: Connection source '{src}' not in nodes")
            for conn_type, outputs in conn_map.items():
                for output_group in outputs:
                    for target in output_group:
                        target_node = target.get("node")
                        if target_node not in node_names:
                            errors.append(f"{relpath}: Connection target '{target_node}' not in nodes")

    if errors:
        print(f"Validation FAILED with {len(errors)} errors:")
        for err in errors:
            print(f" - {err}")
        sys.exit(1)
    else:
        print("✅ All 62 workflow templates validated successfully with 0 errors!")

if __name__ == "__main__":
    validate()
