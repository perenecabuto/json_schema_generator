# coding: utf-8

import os

from unittest import TestCase
from test_api.record import record

import mock


class RecordTest(TestCase):

    def test_should_generate_a_python_code_with_a_verification_upon_a_service(self):
        python_filepath, python_filename = os.path.split(__file__)
        python_filepath = os.path.join(python_filepath, 'example.py')
        record('http://json-schema.org/example', python_filepath)

        self.assertTrue(os.path.exists(python_filepath))