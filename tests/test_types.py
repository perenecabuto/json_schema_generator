# -*- coding: utf-8 -*-

import sys
from unittest import TestCase

from json_schema_generator.schema_types import (
    Type,
    NullType,
    StringType,
    NumberType,
    BooleanType,
    ArrayType,
    ObjectType,
)


class TestSchemaTypes(TestCase):
    if sys.version_info < (2, 7):
        def assertIsInstance(self, obj, *types):
            assert isinstance(obj, types)

        def assertIn(self, key, iterable):
            assert key in iterable


    def test_schema_verion(self):
        self.assertEqual(Type.schema_version, "http://json-schema.org/draft-03/schema")

    def test_integer_type(self):
        gotten = Type.get_schema_type_for(type(1))

        self.assertEqual(gotten, NumberType)
        self.assertEqual(gotten.json_type, "number")

    def test_float_type(self):
        gotten = Type.get_schema_type_for(type(1.1))

        self.assertEqual(gotten, NumberType)
        self.assertEqual(gotten.json_type, "number")

    if sys.version_info < (3,):
        def test_long_type(self):
            gotten = Type.get_schema_type_for(long)

            self.assertEqual(gotten, NumberType)
            self.assertEqual(gotten.json_type, "number")

    def test_string_type(self):
        gotten = Type.get_schema_type_for(type("str"))

        self.assertEqual(gotten, StringType)
        self.assertEqual(gotten.json_type, "string")

    def test_unicode_type(self):
        gotten = Type.get_schema_type_for(type(u"str"))

        self.assertEqual(gotten, StringType)
        self.assertEqual(gotten.json_type, "string")

    def test_null_type(self):
        gotten = Type.get_schema_type_for(type(None))

        self.assertEqual(gotten, NullType)
        self.assertEqual(gotten.json_type, "null")

    def test_boolean_type(self):
        gotten = Type.get_schema_type_for(type(True))

        self.assertEqual(gotten, BooleanType)
        self.assertEqual(gotten.json_type, "boolean")

    def test_array_type(self):
        gotten = Type.get_schema_type_for(type([]))

        self.assertEqual(gotten, ArrayType)
        self.assertEqual(gotten.json_type, "array")
        self.assertIn("items", dir(gotten))

    def test_object_type(self):
        gotten = Type.get_schema_type_for(type({}))

        self.assertEqual(gotten, ObjectType)
        self.assertEqual(gotten.json_type, "object")
        self.assertIn("properties", dir(gotten))

