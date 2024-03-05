#!/usr/bin/python3
"""
Script to add all arguments to a Python list and then save them to a JSON file
"""


import sys
import json
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file.py").load_from_json_file


# def save_arguments(filename):
filename = "add_item.json"
args_list = []

for arg in sys.argv[1:]:
    args_list.append(arg)

save_to_json_file(args_list, filename)