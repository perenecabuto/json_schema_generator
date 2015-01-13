# -*- coding: utf-8 -*-

import json, sys
from unittest import TestCase

from json_schema_generator import SchemaGenerator

from .helpers import normalize_json
from . import fixtures


class TestGenerator(TestCase):
    if sys.version_info < (2, 7):
        def assertIsInstance(self, obj, *types):
            assert isinstance(obj, types)

        def assertIn(self, key, iterable):
            assert key in iterable

    def test_conversion(self):
        generator = SchemaGenerator.from_json(fixtures.json_1)

        gotten = generator.to_dict()
        expected = json.loads(fixtures.json_schema_1)

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

    def test_generator_should_convert_null(self):
        generator = SchemaGenerator.from_json('null')
        expected = json.loads(fixtures.null_json_schema)

        self.assertEqual(generator.to_dict(), expected)

    def test_generator_should_convert_number(self):
        generator = SchemaGenerator.from_json('1')
        expected = json.loads(fixtures.number_json_schema)

        self.assertEqual(generator.to_dict(), expected)

    def test_generator_should_convert_string(self):
        generator = SchemaGenerator.from_json('"str"')
        expected = json.loads(fixtures.string_json_schema)

        self.assertEqual(generator.to_dict(), expected)

    def test_generator_should_convert_boolean(self):
        generator = SchemaGenerator.from_json('true')
        expected = json.loads(fixtures.boolean_json_schema)

        self.assertEqual(generator.to_dict(), expected)

    def test_generator_should_convert_array(self):
        generator = SchemaGenerator.from_json('[]')
        expected = json.loads(fixtures.array_json_schema)

        self.assertEqual(generator.to_dict(), expected)

    def test_generator_should_convert_array_with_homogeneous_items(self):
        generator = SchemaGenerator.from_json('[1, 2, 3]')
        expected = json.loads(fixtures.array_of_number_json_schema)

        self.assertEqual(generator.to_dict(), expected)

    def test_generator_should_convert_array_with_hetereogeneous_items(self):
        generator = SchemaGenerator.from_json('["a", 1, {}]')
        expected = json.loads(fixtures.mixed_array_json_schema)

        self.assertEqual(generator.to_dict(), expected)

    def test_generator_should_convert_object(self):
        generator = SchemaGenerator.from_json('{}')
        expected = json.loads(fixtures.object_json_schema)

        self.assertEqual(generator.to_dict(), expected)

    def test_generator_should_convert_object_with_properties(self):
        generator = SchemaGenerator.from_json('{"p1": 1, "p2": "str", "p3": false}')
        expected = json.loads(fixtures.object_with_properties_schema)

        self.assertEqual(generator.to_dict(), expected)

    def test_generator_should_return_text_plain_json_schema(self):
        generator = SchemaGenerator.from_json('{"p1": 1, "p2": "str", "p3": false}')

        gotten = normalize_json(generator.to_json())
        expected = normalize_json(fixtures.object_with_properties_schema)

        self.assertEqual(gotten, expected)
