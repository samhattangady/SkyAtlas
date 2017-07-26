import unittest

import skyatlas

class TestAdders(unittest.TestCase):

    def setUp(self):
        self.atlas = skyatlas.load_geojson('skyatlas/tests/data/g1.geojson')
        self.assertIsInstance(self.atlas, skyatlas.SkyAtlas, 
            'TestAdders assumes load_geojson is working')

    def test_add_point(self):
        point = self.atlas.points[0]
        num_points = len(self.atlas.points)

        self.atlas.add_point(point)

        self.assertEqual(len(self.atlas.points), num_points+1, 
            'Number of points did not increase')
        self.assertEqual(point, self.atlas.points[-1],
            'Last point is not the point that was added')

    def test_add_point_disallow_other(self):
        line = self.atlas.lines[0]
        polygon = self.atlas.polygons[0]

        with self.assertRaises(ValueError, 
                msg='add_point allows line to be added as point'):
            self.atlas.add_point(line)
        with self.assertRaises(ValueError, 
                msg='add_point allows polygon to be added as point'):
            self.atlas.add_point(polygon)
        with self.assertRaises(ValueError, 
                msg='add_point allows string to be added as point'):
            self.atlas.add_point('str')
        with self.assertRaises(ValueError, 
                msg='add_point allows int to be added as point'):
            self.atlas.add_point(5)

    def test_add_line(self):
        line = self.atlas.lines[0]
        num_lines = len(self.atlas.lines)

        self.atlas.add_line(line)

        self.assertEqual(len(self.atlas.lines), num_lines+1, 
            'Number of lines did not increase')
        self.assertEqual(line, self.atlas.lines[-1],
            'Last line is not the line that was added')

    def test_add_line_disallow_other(self):
        point = self.atlas.points[0]
        polygon = self.atlas.polygons[0]

        with self.assertRaises(ValueError, 
                msg='add_line allows point to be added as line'):
            self.atlas.add_line(point)
        with self.assertRaises(ValueError, 
                msg='add_line allows polygon to be added as line'):
            self.atlas.add_line(polygon)
        with self.assertRaises(ValueError, 
                msg='add_line allows string to be added as line'):
            self.atlas.add_line('str')
        with self.assertRaises(ValueError, 
                msg='add_line allows int to be added as line'):
            self.atlas.add_line(5)

    def test_add_polygon(self):
        polygon = self.atlas.polygons[0]
        num_polygons = len(self.atlas.polygons)

        self.atlas.add_polygon(polygon)

        self.assertEqual(len(self.atlas.polygons), num_polygons+1, 
            'Number of polygons did not increase')
        self.assertEqual(polygon, self.atlas.polygons[-1],
            'Last polygon is not the polygon that was added')

    def test_add_polygon_disallow_other(self):
        point = self.atlas.points[0]
        line = self.atlas.lines[0]

        with self.assertRaises(ValueError, 
                msg='add_polygon allows point to be added as polygon'):
            self.atlas.add_polygon(point)
        with self.assertRaises(ValueError, 
                msg='add_polygon allows line to be added as polygon'):
            self.atlas.add_polygon(line)
        with self.assertRaises(ValueError, 
                msg='add_polygon allows string to be added as polygon'):
            self.atlas.add_polygon('str')
        with self.assertRaises(ValueError, 
                msg='add_polygon allows int to be added as polygon'):
            self.atlas.add_polygon(5)

    def test_add_feature(self):
        point = self.atlas.points[0]
        line = self.atlas.lines[0]
        polygon = self.atlas.polygons[0]
        num_points = len(self.atlas.points)
        num_lines = len(self.atlas.lines)
        num_polygons = len(self.atlas.polygons)

        self.atlas.add_feature(point)
        self.atlas.add_feature(line)
        self.atlas.add_feature(polygon)

        self.assertEqual(len(self.atlas.points), num_points+1, 
            'Number of points did not increase')
        self.assertEqual(point, self.atlas.points[-1],
            'Last point is not the point that was added')
        self.assertEqual(len(self.atlas.lines), num_lines+1, 
            'Number of lines did not increase')
        self.assertEqual(line, self.atlas.lines[-1],
            'Last line is not the line that was added')
        self.assertEqual(len(self.atlas.polygons), num_polygons+1, 
            'Number of polygons did not increase')
        self.assertEqual(polygon, self.atlas.polygons[-1],
            'Last polygon is not the polygon that was added')

    def test_add_feature_disallow_others(self):
        with self.assertRaises(ValueError, 
                msg='add_feature allows string to be added as feature'):
            self.atlas.add_feature('self.atlas.points[0]')
        with self.assertRaises(ValueError, 
                msg='add_feature allows int to be added as feature'):
            self.atlas.add_feature(5)

