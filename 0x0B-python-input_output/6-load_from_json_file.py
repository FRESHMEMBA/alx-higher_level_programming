#!/usr/bin/python3
"""
Defines a funtion that creates an Object from a JSON file.
"""


import json


def load_from_json(filename):
    with open(filename) as file:
        return json.load(file)
