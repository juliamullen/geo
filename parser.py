import json
import gzip
import os

from biothings import config
logger = config.logger

def load_annotations(data_folder):
    json_path = os.path.join(data_folder, "shapefiles.json.gz")
    with gzip.open(json_path) as f:
        yield from json.loads(f.read().decode('utf-8'))
