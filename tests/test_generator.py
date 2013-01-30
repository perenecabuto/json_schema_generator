# -*- coding: utf-8 -*-

from unittest import TestCase

try:
    from simplejson import simplejson as json
except:
    import json

from generator import SchemaGenerator

import fixtures


class TestGenerator(TestCase):

    def test_conversion(self):
        generator = SchemaGenerator.from_json(fixtures.json_1)

        gotten = generator.to_dict()
        expected = json.loads(fixtures.json_schema_1)

        from pprint import pprint
        pprint(gotten)

        self.assertEqual(gotten, expected)

    def test_instance(self):
        schema_dict = json.loads(fixtures.json_schema_1)
        generator = SchemaGenerator(schema_dict)

        self.assertIsInstance(generator, SchemaGenerator)
        self.assertEqual(generator.base_object, schema_dict)

    def test_base_object_from_json_should_match_the_submitted(self):
        schema_dict = json.loads(fixtures.json_schema_1)
        generator = SchemaGenerator.from_json(fixtures.json_schema_1)

        self.assertIsInstance(generator, SchemaGenerator)
        self.assertEqual(generator.base_object, schema_dict)

    def test_generator_should_instanciate_from_json(self):
        generator = SchemaGenerator.from_json(fixtures.json_1)

        self.assertIsInstance(generator, SchemaGenerator)

    def test_generator_should_convert_null_types(self):
        generator = SchemaGenerator.from_json('null')
        expected = json.loads(fixtures.null_json_schema)

        self.assertEqual(generator.to_dict(), expected)

    def test_generator_should_convert_number_types(self):
        generator = SchemaGenerator.from_json('1')
        expected = json.loads(fixtures.number_json_schema)

        self.assertEqual(generator.to_dict(), expected)

    def test_generator_should_convert_string_types(self):
        generator = SchemaGenerator.from_json('"str"')
        expected = json.loads(fixtures.string_json_schema)

        self.assertEqual(generator.to_dict(), expected)

    def test_generator_should_convert_boolean_types(self):
        generator = SchemaGenerator.from_json('true')
        expected = json.loads(fixtures.boolean_json_schema)

        self.assertEqual(generator.to_dict(), expected)

