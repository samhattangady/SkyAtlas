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

from .classes import SkyAtlas
from .loaders import load_geojson
