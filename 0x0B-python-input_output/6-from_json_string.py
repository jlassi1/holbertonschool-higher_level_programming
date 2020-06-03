#!/usr/bin/python3
"""module"""
import json


def from_json_string(my_str):
    """unction that returns the JSON representation of an object (string)"""
    return json.loads(my_str)
