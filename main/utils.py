import json
from data.conf import FILE_JSON


def load_file_json():
    with open(FILE_JSON, 'r', encoding='utf-8') as file:
        return json.load(file)

