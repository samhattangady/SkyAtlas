import unittest

import skyatlas


class TestCoords(unittest.TestCase):

    def setUp(self):
        self.atlas = skyatlas.load_geojson('skyatlas/tests/data/g1.geojson')
        self.assertIsInstance(self.atlas, skyatlas.SkyAtlas, 
            'TestCoords assumes load_geojson is working')

    def test_points_coords(self):
        points_coords = self.atlas.points.coords()

        self.assertEqual(len(points_coords), len(self.atlas.points),
            'Number of coords is not equal to number of points')

    def test_point_coords_default_with_z(self):
        point = self.atlas.points[0]

        self.assertEqual(len(point.coords()), len(point.coords(z=True)),
            'Default behaviour of coords is not same as z=True')

    def test_point_coords_without_z(self):
        point = self.atlas.points[0]

        self.assertEqual(len(point.coords(z=False)), 2,
            'coords(z=False) is not giving 2 values')

    def test_lines_coords(self):
        lines_coords = self.atlas.lines.coords()

        self.assertEqual(len(lines_coords), len(self.atlas.lines),
            'Number of coords is not equal to number of lines')

    def test_line_coords_default_with_z(self):
        line = self.atlas.lines[0]

        self.assertEqual(len(line.coords()[0]), len(line.coords(z=True)[0]),
            'Default behaviour of coords is not same as z=True')

    def test_line_coords_without_z(self):
        line = self.atlas.lines[0]

        self.assertEqual(len(line.coords(z=False)[0]), 2,
            'coords(z=False) is not giving 2 values')

    def test_polygons_coords(self):
        polygons_coords = self.atlas.polygons.coords()

        self.assertEqual(len(polygons_coords), len(self.atlas.lines),
            'Number of coords is not equal to number of polygons')

    def test_polygon_coords_default_with_z(self):
        polygon = self.atlas.polygons[0]

        self.assertEqual(len(polygon.coords()[0]), len(polygon.coords(z=True)[0]),
            'Default behaviour of coords is not same as z=True')

    def test_polygon_coords_without_z(self):
        polygon = self.atlas.polygons[0]

        self.assertEqual(len(polygon.coords(z=False)[0]), 2,
            'coords(z=False) is not giving 2 values')

    def test_features_coords(self):
        points_coords = self.atlas.points.coords()
        lines_coords = self.atlas.lines.coords()
        polygons_coords = self.atlas.polygons.coords()

        feature_coords = self.atlas.features.coords()

        for coord in points_coords:
            self.assertIn(coord, feature_coords, 
                'all point coords are not in feature coords')
        for coord in lines_coords:
            self.assertIn(coord, feature_coords, 
                'all line coords are not in feature coords')
        for coord in polygons_coords:
            self.assertIn(coord, feature_coords, 
                'all polygon coords are not in feature coords')
        self.assertEqual(len(feature_coords), len(points_coords+lines_coords+polygons_coords),
            'number of coords in different in features and sum of lines,points,polygons')
