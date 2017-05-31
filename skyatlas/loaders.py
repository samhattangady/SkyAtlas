import json
import os

from .classes import SkyAtlas

def load_geojson(json_in):
    # TODO Check what else are the possible inputs here
    if type(json_in) == str:
        if os.path.isfile(json_in):
            with open(json_in) as in_file:
                geojson_data = json.load(in_file)
        else:
            geojson_data = json.loads(json_in)
    elif type(json_in) == dict:
        geojson_data = json_in
    else:
        # TODO Throw exception
        return None
    return SkyAtlas().load_geojson(geojson_data)

def load(input):
    # TODO parse input, call corresponding load function
    pass