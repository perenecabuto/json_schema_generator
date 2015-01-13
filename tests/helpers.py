# -*- coding: utf-8 -*-

import json


def normalize_json(json_str):
    return json.dumps(json.loads(json_str), sort_keys=True)

