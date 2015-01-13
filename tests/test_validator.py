# -*- coding: utf-8 -*-

import os
import json

from unittest import TestCase

from . import fixtures
from json_schema_generator import Validator


class TestValidator(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.json_schema_file_path = os.path.join(os.path.dirname(__file__), 'tmp', 'test.json_schema')

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.json_schema_file_path):
            os.remove(cls.json_schema_file_path)

    def test_validator_should_certify_json(self):
        json_schema_dict = json.loads(fixtures.json_schema_1)
        validator = Validator(json_schema_dict)

        gotten = validator.assert_json(fixtures.json_1)

        self.assertEqual(gotten, True)

    def test_validator_should_certify_json_from_schema_file(self):
        with open(self.json_schema_file_path, 'w') as jss_file:
            jss_file.write(fixtures.json_schema_1)

        validator = Validator.from_path(self.json_schema_file_path)

        gotten = validator.assert_json(fixtures.json_1)

        self.assertEqual(gotten, True)

