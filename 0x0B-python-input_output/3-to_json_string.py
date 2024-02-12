#!/usr/bin/python3
"""
Defines a function that returns the JSON represenetation of an object (string)
"""


import json

def to_json_string(my_obj):
    
    return json.dumps(my_obj)