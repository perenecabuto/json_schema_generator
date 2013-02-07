# -*- coding: utf-8 -*-

import json
from .schema_types import Type, ObjectType, ArrayType


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

    def to_dict(self, base_object=None, object_id=None, first_level=True):
        """docstring for to_dict"""

        schema_dict = {}

        if first_level:
            base_object = self.base_object
            schema_dict["$schema"] = Type.schema_version
            schema_dict["id"] = "#"

        if object_id is not None:
            schema_dict["id"] = str(object_id)

        base_object_type = type(base_object)
        schema_type = Type.get_schema_type_for(base_object_type)

        schema_dict["required"] = True
        schema_dict["type"] = schema_type.json_type

        if schema_type == ObjectType and len(base_object) > 0:
            schema_dict["properties"] = {}

            for prop, value in base_object.items():
                schema_dict["properties"][prop] = self.to_dict(value, prop, False)

        elif schema_type == ArrayType and len(base_object) > 0:
            first_item_type = type(base_object[0])
            same_type = all((type(item) == first_item_type for item in base_object))

            if same_type:
                schema_dict['items'] = self.to_dict(base_object[0], 0, False)

            else:
                schema_dict['items'] = []

                for idx, item in enumerate(base_object):
                    schema_dict['items'].append(self.to_dict(item, idx, False))

        return schema_dict

    def to_json(self, **kwargs):
        return json.dumps(self.to_dict(), **kwargs)

