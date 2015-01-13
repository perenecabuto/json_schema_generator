# -*- coding: utf-8 -*-

import os
import json

from unittest import TestCase
from fudge import patch
from . import fixtures

from json_schema_generator import Recorder


class TestRecorder(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.service_url = 'http://fake_url/with.json'
        cls.json_schema_file_path = os.path.join(os.path.dirname(__file__), 'tmp', 'test.json_schema')

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.json_schema_file_path):
            os.remove(cls.json_schema_file_path)

    @patch('six.moves.urllib.request.urlopen')
    def test_recorder_should_get_json_from_url(self, fake_urlopen=None):
        fake_urlopen.is_callable().expects_call().returns_fake() \
            .provides('read').returns(fixtures.json_1)

        rec = Recorder.from_url(self.service_url)
        rec.save_json_schema(self.json_schema_file_path)

        expected = json.loads(fixtures.json_schema_1)
        gotten = json.load(open(self.json_schema_file_path))

        self.assertEqual(gotten, expected)
