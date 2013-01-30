# -*- coding: utf-8 -*-

import json
from json_schema_types import Type, ObjectType, ArrayType


class SchemaGenerator(object):

    def __init__(self, base_object):
        """docstring for __init__"""

        self._base_object = base_object

    @property
    def base_object(self):
        """docstring for base_object"""

        return self._base_object

    @classmethod
    def from_json(cls, base_json):
        """docstring for from_json"""

        base_object = json.loads(base_json)
        obj = cls(base_object)

        return obj

    def to_dict(self, base_object=None):
        """docstring for to_dict"""

        schema_dict = {}

        if not base_object:
            base_object = self.base_object
            schema_dict["$schema"] = Type.schema_version
            schema_dict["id"] = "#"

        base_object_type = type(base_object)
        schema_type = Type.get_schema_type_for(base_object_type)

        schema_dict["required"] = True
        schema_dict["type"] = schema_type.json_type

        if schema_type == ObjectType:
            pass

        elif schema_type == ArrayType:
            if len(base_object) > 0:
                first_item_type = type(base_object[0])
                same_type = all(base_object, lambda item: type(item) == first_item_type)
                schema_dict['']

        return schema_dict

