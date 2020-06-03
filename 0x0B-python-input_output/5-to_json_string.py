#!/usr/bin/python3
"""module"""
import json


def to_json_string(my_obj):
    """unction that returns the JSON representation of an object (string)"""
    if not json.dumps(my_obj):
        raise Exception("{} is not JSON serializable".format(str(my_obj)))
    return json.dumps(my_obj)
