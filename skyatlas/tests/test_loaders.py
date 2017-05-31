import json
import unittest

import skyatlas
from skyatlas.classes import SkyAtlas


class TestLoaders(unittest.TestCase):

    def test_load_geojson_feature_collection(self):
        feature_collection_path = 'skyatlas/tests/data/g1.geojson'

        atlas = skyatlas.load_geojson(feature_collection_path)

        self.assertIsInstance(atlas, SkyAtlas, 'load_geojson did not return SkyAtlas object')
        self.assertEqual(len(atlas.points), 1, 'points were loaded incorrectly')
        self.assertEqual(len(atlas.features), 3, 'features were loaded incorrectly')

    def test_load_from_string(self):
        feature_collection_path = 'skyatlas/tests/data/g1.geojson'
        with open(feature_collection_path) as geojson_file:
            geojson_string = geojson_file.read()

        atlas = skyatlas.load_geojson(geojson_string)

        self.assertIsInstance(atlas, SkyAtlas, 'load_geojson did not return SkyAtlas object')

    def test_load_from_dict(self):
        feature_collection_path = 'skyatlas/tests/data/g1.geojson'
        with open(feature_collection_path) as geojson_file:
            geojson_dict = json.load(geojson_file)

        atlas = skyatlas.load_geojson(geojson_dict)

        self.assertIsInstance(atlas, SkyAtlas, 'load_geojson did not return SkyAtlas object')