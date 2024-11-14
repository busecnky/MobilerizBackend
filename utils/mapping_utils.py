import json
from pathlib import Path
from functools import reduce

def load_vendor_mapping():
    with open(Path("config/vendor_mappings.json")) as f:
        return json.load(f)

def get_nested_value(data, path):
    keys = path.split('.')
    return reduce(lambda d, key: d.get(key, {}) if isinstance(d, dict) else {}, keys, data)
