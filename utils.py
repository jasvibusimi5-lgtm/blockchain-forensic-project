import hashlib, json, os

def calculate_file_hash(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def calculate_dict_hash(data: dict) -> str:
    data_str = json.dumps(data, sort_keys=True)
    return hashlib.sha256(data_str.encode()).hexdigest()

def save_json(data, filepath):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, default=str)