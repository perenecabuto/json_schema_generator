### JSON Schema Generator

#### About

It is a json schema generator from any json source.

#### Usage

See [Usage](USAGE.md)

#### Example

Since you have a json file with the above structure:
```json
    {
        "item_1": "string_value_1",
        "item_2": 123,
        "item_3": [1, 2, 3],
        "item_4": true,
        "item_5": null,
        "item_6": { "key": "value"},
        "item_7": {
            "item_7.1": "string_value_1",
            "item_7.2": 123,
            "item_7.3": [1, 2, 3],
            "item_7.4": true,
            "item_7.5": null,
            "item_7.6": { "key": "value"}
        }
    }
```
It should generate a json schema as":
```json
    {
        "$schema": "http://json-schema.org/draft-03/schema",
        "id": "#",
        "required": true,
        "type": "object",
        "properties": {
            "item_1": {
                "id": "item_1",
                "required": true,
                "type": "string"
            },
            "item_2": {
                "id": "item_2",
                "required": true,
                "type": "number"
            },
            "item_3": {
                "id": "item_3",
                "required": true,
                "type": "array" ,
                "items": {
                    "id": "0",
                    "required": true,
                    "type": "number"
                }
            },
            "item_4": {
                "id": "item_4",
                "required": true,
                "type": "boolean"
            },
            "item_5": {
                "id": "item_5",
                "required": true,
                "type": "null"
            },
            "item_6": {
                "id": "item_6",
                "required": true,
                "type": "object" ,
                "properties": {
                    "key": {
                        "id": "key",
                        "required": true,
                        "type": "string"
                    }
                }
            },
            "item_7": {
                "id": "item_7",
                "required": true,
                "type": "object" ,
                "properties": {
                    "item_7.1": {
                        "id": "item_7.1",
                        "required": true,
                        "type": "string"
                    },
                    "item_7.2": {
                        "id": "item_7.2",
                        "required": true,
                        "type": "number"
                    },
                    "item_7.3": {
                        "id": "item_7.3",
                        "required": true,
                        "type": "array" ,
                        "items": {
                            "id": "0",
                            "required": true,
                            "type": "number"
                        }
                    },
                    "item_7.4": {
                        "id": "item_7.4",
                        "required": true,
                        "type": "boolean"
                    },
                    "item_7.5": {
                        "id": "item_7.5",
                        "required": true,
                        "type": "null"
                    },
                    "item_7.6": {
                        "id": "item_7.6",
                        "required": true,
                        "type": "object" ,
                        "properties": {
                            "key": {
                                "id": "key",
                                "required": true,
                                "type": "string"
                            }
                        }
                    }
                }
            }
        }
    }
```
