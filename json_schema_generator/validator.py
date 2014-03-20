# -*- coding: utf-8 -*-

import json
from jsonschema import validate


class Validator(object):

    def __init__(self, json_schema_dict):
        self._json_schema_dict = json_schema_dict
        self._error_message = ''

    @property
    def json_schema_dict(self):
        return self._json_schema_dict

    @property
    def error_message(self):
        return self._error_message

    @classmethod
    def from_path(self, path):
        return Validator(json.load(open(path)))

    def assert_json(self, json_str):
        valid = False
        json_object = json.loads(json_str)

        try:
            validate(json_object, self.json_schema_dict)
            valid = True

        except Exception as e:
            self._error_message = "Inválido: \n\t%s" % str(e)

        return valid

