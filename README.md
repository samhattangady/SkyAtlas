# skyatlas
Simplify working with geodata.

Working with a lot of geographic data can lead to a whole bunch of problems. Some choose to store the data in Latitude, Longitude format, while others choose Longitude, Latitude to match with standard geometry's x, y. Some store data in XML format, some in JSON, and still others as CSV. The data is the same, and converting between them is not difficult, just a bit of a hassle. It can also be difficult to use this data in programs or scripts due to the need to dive into specification documents just to extract the point of one polygon from Google Earth.

Skyatlas attempts to solve this problem, by allowing loading of different files, and treating them as the same. It tries to make it easier to extract data, and use it as needed.

## Installation

    # Not currently working. Have to write setup.py etc.
    # Eventually we will add it to pypi for a pip install skyatlas
    pip install git+https://github.com/samhattangady/skyatlas.git

## Usage

Skyatlas is meant to be used with SkyAtlas object.

    # Creating an atlas from geojson
    atlas = skyatlas.load_geojson('path/to/geojson.geojson')
    
Once an atlas object is loaded, you can access all the features, or just a particular type
 
    features = atlas.features
    points = atlas.points
    lines = atlas.lines
    polygons = atlas.lines
    
Internally, the coordinates are stored in the geojson format, but it can be accessed using the `coords()` method.

For the coords of a single feature. Altitude is set to 0 by default

    >>> points[0].coords()
    (77.60988414287567, 12.934377614140951, 0)
    
In case we only want the x and y (longitude and latitude)

    >>> lines[0].coords(z=False)
    [(77.60890245437622, 12.936892417140049), (77.6098895072937, 12.937028351715037), (77.60979294776917, 12.935595806701484), (77.61047959327698, 12.935658546071421), (77.6098895072937, 12.934790650053325), (77.6086127758026, 12.935219370150497), (77.60929942131042, 12.935480784482271)]
    
For the coords of all points in an atlas

    >>> atlas.points.coords(z=False)
    [(77.60890245437622, 12.936892417140049), (77.6098895072937, 12.937028351715037), (77.60979294776917, 12.935595806701484), (77.61047959327698, 12.935658546071421)]
    
Since we are following the GeoJSON specification, we can also access the properties of each feature

    >>> atlas.polygons[0]['properties']
    {'planet': 'Earth', 'hemisphere': 'one of them', 'creatures': ['beluga whales', 'humans', 'potted plants', 'Betelgeusians']}

We can use function to add individual features

    for point in atlas.points:
        if 'blue' in point['properties']['colours']:
            blue_atlas.add_point(point)
    
or all the features in an atlas

    double_points = SkyAtlas()
    double_points.add_points(atlas)
    double_points.add_atlas(atlas)
    
We can create new features

    # Not yet implemented. Have to figure out a straightforward way to do this
    atlas.new_point((77.60890245437622, 12.936892417140049))
    
Finally, it is possible to convert the atlas object to a GeoJSON string to write to file

    with open('points.geojson', 'w') as atlas_out:
        atlas_out.write(double_points.to_geojson())
        

## To be implemented

 - KML + KMZ
 - Shapefiles
 - Input verification
