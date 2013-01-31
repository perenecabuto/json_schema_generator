# -*- coding: utf-8 -*-


null_json_schema = """
    {
        "$schema": "http://json-schema.org/draft-03/schema",
        "type": "null",
        "id": "#",
        "required": true
    }
"""

number_json_schema = """
    {
        "$schema": "http://json-schema.org/draft-03/schema",
        "type": "number",
        "id": "#",
        "required": true
    }
"""

string_json_schema = """
    {
        "$schema": "http://json-schema.org/draft-03/schema",
        "type": "string",
        "id": "#",
        "required": true
    }
"""

boolean_json_schema = """
    {
        "$schema": "http://json-schema.org/draft-03/schema",
        "type": "boolean",
        "id": "#",
        "required": true
    }
"""

boolean_json_schema = """
    {
        "$schema": "http://json-schema.org/draft-03/schema",
        "type": "boolean",
        "id": "#",
        "required": true
    }
"""

array_json_schema = """
    {
        "$schema": "http://json-schema.org/draft-03/schema",
        "type": "array",
        "id": "#",
        "required": true
    }
"""

array_of_number_json_schema = """
    {
        "$schema": "http://json-schema.org/draft-03/schema",
        "type": "array",
        "id": "#",
        "required": true,
        "items":  {
            "id": "0",
            "type": "number",
            "required": true
        }
    }
"""

mixed_array_json_schema = """
    {
        "$schema": "http://json-schema.org/draft-03/schema",
        "type": "array",
        "id": "#",
        "required": true,
        "items":  [
            {
                "id": "0",
                "type": "string",
                "required": true
            },
            {
                "id": "1",
                "type": "number",
                "required": true
            },
            {
                "id": "2",
                "type": "object",
                "required": true
            }
        ]
    }
"""

object_json_schema = """
    {
        "$schema": "http://json-schema.org/draft-03/schema",
        "type": "object",
        "id": "#",
        "required": true
    }
"""

object_with_properties_schema = """
    {
        "$schema": "http://json-schema.org/draft-03/schema",
        "type": "object",
        "id": "#",
        "required": true,
        "properties": {
            "p1": {
                "id": "p1",
                "type": "number",
                "required": true
            },
            "p2": {
                "id": "p2",
                "type": "string",
                "required": true
            },
            "p3": {
                "id": "p3",
                "type": "boolean",
                "required": true
            }
        }
    }
"""

json_1 = """
    {
        "item_1": "string_value_1",
        "item_2": 123,
        "item_3": [1, 2, 3],
        "item_4": true,
        "item_5": null,
        "item_6": {"key": "value"},
        "item_7": {
            "item_7.1": "string_value_1",
            "item_7.2": 123,
            "item_7.3": [1, 2, 3],
            "item_7.4": true,
            "item_7.5": null,
            "item_7.6": {"key": "value"}
        }
    }
"""

json_schema_1 = """
    {
        "type": "object",
        "$schema": "http://json-schema.org/draft-03/schema",
        "id": "#",
        "required": true,
        "properties": {
            "item_1": {
                "type": "string",
                "id": "item_1",
                "required": true
            },
            "item_2": {
                "type": "number",
                "id": "item_2",
                "required": true
            },
            "item_3": {
                "type": "array",
                "id": "item_3",
                "required": true,
                "items": {
                    "type": "number",
                    "id": "0",
                    "required": true
                }
            },
            "item_4": {
                "type": "boolean",
                "id": "item_4",
                "required": true
            },
            "item_5": {
                "type": "null",
                "id": "item_5",
                "required": true
            },
            "item_6": {
                "type": "object",
                "id": "item_6",
                "required": true,
                "properties": {
                    "key": {
                        "type": "string",
                        "id": "key",
                        "required": true
                    }
                }
            },
            "item_7": {
                "type": "object",
                "id": "item_7",
                "required": true,
                "properties": {
                    "item_7.1": {
                        "type": "string",
                        "id": "item_7.1",
                        "required": true
                    },
                    "item_7.2": {
                        "type": "number",
                        "id": "item_7.2",
                        "required": true
                    },
                    "item_7.3": {
                        "type": "array",
                        "id": "item_7.3",
                        "required": true,
                        "items": {
                            "type": "number",
                            "id": "0",
                            "required": true
                        }
                    },
                    "item_7.4": {
                        "type": "boolean",
                        "id": "item_7.4",
                        "required": true
                    },
                    "item_7.5": {
                        "type": "null",
                        "id": "item_7.5",
                        "required": true
                    },
                    "item_7.6": {
                        "type": "object",
                        "id": "item_7.6",
                        "required": true,
                        "properties": {
                            "key": {
                                "type": "string",
                                "id": "key",
                                "required": true
                            }
                        }
                    }
                }
            }
        }
    }
"""

