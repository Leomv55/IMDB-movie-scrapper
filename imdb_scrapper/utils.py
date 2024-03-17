import os
import json
import logging

stdlogger = logging.getLogger(__name__)


def write_to_json(data, output_dir="output", filename="movies.json"):
    if not filename.endswith(".json"):
        filename = filename + ".json"
    os.makedirs(output_dir, exist_ok=True)

    with open(f"{output_dir}/{filename}", "w") as json_file:
        json.dump(data, json_file, indent=4)
        json_file.close()

    return json_file
