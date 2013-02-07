# -*- coding: utf-8 -*-

import os
import json

from unittest import TestCase
from fudge import patch

import fixtures


class TestCertifier(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.service_url = 'http://search.twitter.com/search.json?q=blue%20angels&rpp=5&include_entities=true&result_type=mixed'
        cls.json_schema_file_path = os.path.join(os.path.dirname(__file__), 'tmp', 'test.json_schema')

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.json_schema_file_path)

    @patch('urllib2.urlopen')
    def test_recorder_should_get_json_from_url(self, fake_urlopen=None):
        from json_certifier.recorder import Recorder

        fake_urlopen_read = fake_urlopen.is_callable().expects_call().returns_fake()
        fake_urlopen_read.provides('read').returns(fixtures.json_1)

        rec = Recorder.from_url(self.service_url)
        rec.save_json_schema(self.json_schema_file_path)

        expected = json.loads(fixtures.json_schema_1)
        gotten = json.load(open(self.json_schema_file_path))

        self.assertEqual(gotten, expected)

