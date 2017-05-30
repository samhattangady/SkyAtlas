__author__ = 'Samarth Hattangady <samhattangady@gmail.com>'

"""
SkyAtlas is a python module to easily work with different geodata
files.

It is an attempt to make it easier to draw data out of the files and 
manipulate it. It treats the different shapes, ie, points, lines and
polygons as separate entities, that are referred to as attributes of
the atlas object. There is also a features attribute that is a 
concatenation of the points, lines and polygons lists.

The storage of points is modelled around GeoJSON. So each feature has
coordinates and properties as defined by GeoJSON specifications.

The core functionality is provided by the `coords()` method. This gives
the coordinates in latitude and longitude of lists of features or 
induvidual features. The idea behind this is that the coordinates of
all the points in an atlas object can accessed by `atlas.points.coords()`
This will give a list of tuples, which represent the coordinates of
each point.

Eventually there will be support to convert between different formats.
The proposed formats are GeoJSON, KML+KMZ and shapefiles.
"""

import json
import os 

from .classes import SkyAtlas

def load_geojson(json_in):
    # TODO Check what else are the possible inputs here
    if os.path.isfile(json_in):
        with open(json_in) as in_file:
            geojson_data = json.load(in_file)
    elif type(json_in) == str:
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