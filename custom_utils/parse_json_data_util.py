import json


def parse_json_data(json_data):
    try:
        return json.loads(json_data)
    except json.decoder.JSONDecodeError:
        return json_data
