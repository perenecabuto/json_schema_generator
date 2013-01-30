# -*- coding: utf-8 -*-

from unittest import TestCase

try:
    from simplejson import simplejson as json
except:
    import json

from generator import SchemaGenerator
from .fixtures import example_json_1, example_json_schema_1


class TestGenerator(TestCase):

    def test_conversion(self):
        generator = SchemaGenerator.from_json(example_json_1)

        gotten = generator.to_dict()
        expected = json.loads(example_json_schema_1)

        from pprint import pprint
        pprint(gotten)

        self.assertEqual(gotten, expected)

    def test_instance(self):
        schema_dict = json.loads(example_json_schema_1)
        generator = SchemaGenerator(schema_dict)

        self.assertIsInstance(generator, SchemaGenerator)
        self.assertEqual(generator.base_object, schema_dict)

    def test_base_object_from_json_should_match_the_submitted(self):
        schema_dict = json.loads(example_json_schema_1)
        generator = SchemaGenerator.from_json(example_json_schema_1)

        self.assertIsInstance(generator, SchemaGenerator)
        self.assertEqual(generator.base_object, schema_dict)

    def test_generator_should_instanciate_from_json(self):
        generator = SchemaGenerator.from_json(example_json_1)

        self.assertIsInstance(generator, SchemaGenerator)

