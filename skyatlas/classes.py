import json


class SkyGeo(dict):
    def _load_geojson(self, feature):
        self['coordinates'] = feature['geometry']['coordinates']
        self['properties'] = feature['properties']
        return self

    def _to_geojson(self):
        return {
            'type': 'Feature',
            'geometry': {
                'type': self.__type__,
                'coordinates': self['coordinates']
            },
            'properties': self['properties']
        }


class SkyPoint(SkyGeo):
    __type__ = 'Point'

    def _load_geojson(self, feature):
        super()._load_geojson(feature)
        if len(self['coordinates']) == 2:
            self['coordinates'].append(0)
        return self

    def coords(self, z=True):
        # Dict to find end index based on z value
        end = {True: 3, False: 2}[z]
        return tuple(self['coordinates'][:end])


class SkyLine(SkyGeo):
    __type__ = 'LineString'

    def _load_geojson(self, feature):
        super()._load_geojson(feature)
        for coord in self['coordinates']:
            if len(coord) == 2:
                coord.append(0)
        return self

    def coords(self, z=True):
        end = {True: 3, False: 2}[z]
        return [tuple(coord[:end]) for coord in self['coordinates']]


class SkyPolygon(SkyGeo):
    __type__ = 'Polygon'

    def _load_geojson(self, feature):
        super()._load_geojson(feature)
        for poly in self['coordinates']:
            for coord in poly:
                if len(coord) == 2:
                    coord.append(0)
        return self

    def _outer_coords(self, z):
        end = {True: 3, False: 2}[z]
        return [tuple(coord[:end]) for coord in self['coordinates'][0]]

    def _all_coords(self, z):
        end = {True: 3, False: 2}[z]
        return [tuple(coord[:end]) for ring in self['coordinates'] for coord in ring]

    def coords(self, z=True, include_holes=False):
        if include_holes:
            return self._all_coords(z)
        return self._outer_coords(z)


class SkyList(list):
    def coords(self, z=True, *args, **kwargs):
        return [feature.coords(z=z) for feature in self]

    def _to_geojson(self):
        return [feature._to_geojson() for feature in self]


class SkyAtlas(object):
    def __init__(self):
        self._features = SkyList()

    def __str__(self):
        return '<SkyAtlas object with {} points, {} lines and {} polygons>'.format(
            len(self.points), len(self.lines), len(self.polygons))

    @property
    def features(self):
        return self._features

    @property
    def points(self):
        return SkyList([feature for feature in self.features if isinstance(feature, SkyPoint)])

    @property
    def lines(self):
        return SkyList([feature for feature in self.features if isinstance(feature, SkyLine)])

    @property
    def polygons(self):
        return SkyList([feature for feature in self.features if isinstance(feature, SkyPolygon)])

    def load_geojson(self, geojson_data):
        for feature in geojson_data['features']:
            if feature['geometry']['type'] == 'Point':
                self._add_geojson_point(feature)
            elif feature['geometry']['type'] == 'LineString':
                self._add_geojson_line(feature)
            elif feature['geometry']['type'] == 'Polygon':
                self._add_geojson_polygon(feature)
        return self

    def add_point(self, point):
        if isinstance(point, SkyPoint):
            self._features.append(point)
        else:
            error_message = 'point was of type {t}.\n'\
            'Should be of type SkyPoint'.format(t=type(point))
            raise ValueError(error_message)

    def add_line(self, line):
        if isinstance(line, SkyLine):
            self._features.append(line)
        else:
            error_message = 'line was of type {t}.\n'\
            'Should be of type SkyLine'.format(t=type(line))
            raise ValueError(error_message)

    def add_polygon(self, polygon):
        if isinstance(polygon, SkyPolygon):
            self._features.append(polygon)
        else:
            error_message = 'polygon was of type {t}.\n'\
            'Should be of type SkyPolygon'.format(t=type(polygon))
            raise ValueError(error_message)

    def add_feature(self, feature):
        if isinstance(feature, SkyPoint):
            self.add_point(feature)
        elif isinstance(feature, SkyLine):
            self.add_line(feature)
        elif isinstance(feature, SkyPolygon):
            self.add_polygon(feature)
        else:
            error_message = 'feature was of type {t}.\n'\
            'Should be SkyPoint, SkyLine or SkyPolygon'.format(t=type(feature))
            raise ValueError(error_message)

    def add_points(self, atlas):
        self._features.extend(atlas.points)

    def add_lines(self, atlas):
        self._features.extend(atlas.lines)

    def add_polygons(self, atlas):
        self._features.extend(atlas.polygons)

    def add_atlas(self, atlas):
        self.add_points(atlas)
        self.add_lines(atlas)
        self.add_polygons(atlas)

    def to_geojson(self):
        geojson = self._get_empty_geojson()
        geojson['features'].extend(self.features._to_geojson())
        return json.dumps(geojson)

    def _add_geojson_point(self, feature):
        self._features.append(SkyPoint()._load_geojson(feature))

    def _add_geojson_line(self, feature):
        self._features.append(SkyLine()._load_geojson(feature))

    def _add_geojson_polygon(self, feature):
        self._features.append(SkyPolygon()._load_geojson(feature))

    def _get_empty_geojson(self):
        return {
            "type": "FeatureCollection",
            "features": []
        }

