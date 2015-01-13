# -*- coding: utf-8 -*-

import json
from .schema_types import Type, ObjectType, ArrayType, NullType


def json_path(obj, *args):
    if not obj:
        return None

    for arg in args:
        if arg not in obj:
            return None
        obj = obj[arg]
    return obj

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

    def to_dict(self, base_object=None, object_id=None, first_level=True, required = True, nullable = False):
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

        schema_dict["required"] = required
        if nullable:
            schema_dict["type"] = [ schema_type.json_type, NullType.json_type ]
        else:
            schema_dict["type"] = schema_type.json_type

        if schema_type == ObjectType and len(base_object) > 0:
            schema_dict["properties"] = {}

            for prop, value in base_object.items():
                schema_dict["properties"][prop] = self.to_dict(value, prop, False, required, nullable)

        elif schema_type == ArrayType and len(base_object) > 0:
            first_item_type = type(base_object[0])
            same_type = all((type(item) == first_item_type for item in base_object))

            if same_type:
                schema_dict['items'] = self.to_dict(base_object[0], 0, False, required, nullable)

            else:
                schema_dict['items'] = []

                for idx, item in enumerate(base_object):
                    schema_dict['items'].append(self.to_dict(item, idx, False, required, nullable))

        return schema_dict

    @classmethod
    def set_required(cls, schema_dict, full_path, required, nullable = False):
        obj = schema_dict['properties']
        for path_part in full_path[:-1]:
            if obj[path_part]['type'] == ArrayType.json_type or obj[path_part]['type'] == [ ArrayType.json_type, NullType.json_type ]:
                obj = obj[path_part]['items']['properties']
            else:
                obj = obj[path_part]['properties']

        obj = obj[full_path[-1]]

        obj['required'] = required

        if nullable:
            if obj['type'] == ArrayType.json_type and json_path(obj, 'items', 'type'):
                obj['items']['type'] = [ obj['items']['type'], NullType.json_type ]

            if isinstance(obj['type'], list):
                if NullType.json_type not in obj['type']:
                    obj['type'].append(NullType.json_type)
            else:
                obj['type'] = [ obj['type'], NullType.json_type ]
        else:
            if obj['type'] == ArrayType.json_type and json_path(obj, 'items', 'type'):
                if isinstance(obj['items']['type'], list) and len(obj['items']['type']) > 1:
                    obj['items']['type'] = [ x for x in obj['items']['type'] if x != NullType.json_type ]
                    if len(obj['items']['type']) == 1:
                        obj['items']['type'] = obj['items']['type'][0]

            if isinstance(obj['type'], list) and NullType.json_type in obj['type']:
                obj['type'] = obj['type'][0]


    def to_json(self, **kwargs):
        required = kwargs.pop('required', True)
        nullable = kwargs.pop('nullable', False)
        return json.dumps(self.to_dict(required=required, nullable=nullable), **kwargs)

