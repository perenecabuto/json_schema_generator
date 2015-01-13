# -*- coding: utf-8 -*-

import copy
import json
import os
import unittest
import jsonschema

from json_schema_generator import SchemaGenerator

class TestIntegration(unittest.TestCase):
    example_obj = {
        'string' : 'string',
        'number' : 1.0,
        'obj' : {
            'array_number' : [ 1, 2 ],
            'array_obj' : [ { "string" : "string", "number" : 1 } ],
        },
        'array_obj' : [ { "string" : "string" } ],
    }

    def test_happy_path(self):
        schema_dict, obj1 = self.generate_schema_dict(self.example_obj)
        jsonschema.validate(obj1, schema_dict)

    def test_extra_data_passes(self):
        schema_dict, obj1 = self.generate_schema_dict(self.example_obj)
        obj1['newvalue'] = 1.0

        jsonschema.validate(obj1, schema_dict)

    def test_checks_object_types(self):
        schema_dict, obj1 = self.generate_schema_dict(self.example_obj)
        obj1['string'] = 1.0

        self.assertRaises(jsonschema.ValidationError, jsonschema.validate, obj1, schema_dict)

    def test_set_not_required__simple_obj(self):
        schema_dict, obj1 = self.generate_schema_dict(self.example_obj, path_list = [
            [ 'number', ],
            [ 'obj', 'array_number', ],
            [ 'obj', 'array_obj', 'string', ],
            [ 'array_obj', 'string', ],
        ], required = False)

        jsonschema.validate(obj1, schema_dict)

        obj1.pop('number')
        jsonschema.validate(obj1, schema_dict)

        obj1['number'] = None
        self.assertRaises(jsonschema.ValidationError, jsonschema.validate, obj1, schema_dict)

        obj1['number'] = 'string'
        self.assertRaises(jsonschema.ValidationError, jsonschema.validate, obj1, schema_dict)

    def test_set_not_required__nested_array(self):
        schema_dict, obj1 = self.generate_schema_dict(self.example_obj, path_list = [
            [ 'number', ],
            [ 'obj', 'array_number', ],
            [ 'obj', 'array_obj', 'string', ],
            [ 'array_obj', 'string', ],
        ], required = False)

        jsonschema.validate(obj1, schema_dict)

        obj1['obj'].pop('array_number')
        jsonschema.validate(obj1, schema_dict)

        obj1['obj']['array_number'] = None
        self.assertRaises(jsonschema.ValidationError, jsonschema.validate, obj1, schema_dict)

        obj1['obj']['array_number'] = [ 'string' ]
        self.assertRaises(jsonschema.ValidationError, jsonschema.validate, obj1, schema_dict)

    def test_set_not_required__nested_obj(self):
        schema_dict, obj1 = self.generate_schema_dict(self.example_obj, path_list = [
            [ 'number', ],
            [ 'obj', 'array_number', ],
            [ 'obj', 'array_obj', 'string', ],
            [ 'array_obj', 'string', ],
        ], required = False)

        jsonschema.validate(obj1, schema_dict)

        obj1['obj']['array_obj'][0].pop('string')
        jsonschema.validate(obj1, schema_dict)

        obj1['obj']['array_obj'][0]['string'] = None
        self.assertRaises(jsonschema.ValidationError, jsonschema.validate, obj1, schema_dict)

        obj1['obj']['array_obj'][0]['string'] = [ 1.0 ]
        self.assertRaises(jsonschema.ValidationError, jsonschema.validate, obj1, schema_dict)

        obj1['obj'].pop('array_obj')
        self.assertRaises(jsonschema.ValidationError, jsonschema.validate, obj1, schema_dict)

    def test_set_not_required_and_nullable(self):
        schema_dict, obj1 = self.generate_schema_dict(self.example_obj, path_list = [
            [ 'number', ],
            [ 'obj', 'array_number', ],
            [ 'obj', 'array_obj', 'string', ],
            [ 'array_obj', 'string', ],
        ], required = False, nullable = True)

        jsonschema.validate(obj1, schema_dict)

        obj1['obj']['array_obj'][0].pop('string')
        jsonschema.validate(obj1, schema_dict)

        obj1['obj']['array_obj'][0]['string'] = None
        jsonschema.validate(obj1, schema_dict)

    def test_set_default_required(self):
        schema_dict, obj1 = self.generate_schema_dict(self.example_obj, path_list = [
            [ 'number', ],
        ], default_required = False, default_nullable = True, required = True, nullable = False)

        jsonschema.validate(obj1, schema_dict)
        jsonschema.validate({ 'number' : 1 }, schema_dict)
        jsonschema.validate({ 'number' : 1, 'string' : None }, schema_dict)

        self.assertRaises(jsonschema.ValidationError, jsonschema.validate, { 'number' : None }, schema_dict)
        self.assertRaises(jsonschema.ValidationError, jsonschema.validate, { 'number' : 'string' }, schema_dict)
        self.assertRaises(jsonschema.ValidationError, jsonschema.validate, { 'number' : 1, 'string' : 1 }, schema_dict)

    def generate_schema_dict(self, example_event, path_list = [], default_required = True, default_nullable = False, required = False, nullable = False):
        schema_dict = SchemaGenerator(example_event).to_dict(required = default_required, nullable = default_nullable)

        for path in path_list:
            SchemaGenerator.set_required(schema_dict, path, required = required, nullable = nullable)

        # Sanity check that the example event still passes validation
        jsonschema.validate(example_event, schema_dict)

        return schema_dict, copy.deepcopy(example_event)
