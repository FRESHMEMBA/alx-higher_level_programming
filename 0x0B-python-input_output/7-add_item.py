#!/usr/bin/python3
"""
This script adds all arguments to a Python list, and then save then to a file.
"""


import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file.py").load_from_json_file

# def save_arguments(filename):
filename = "add_item.json"
args_list = []

for arg in sys.argv[1:]:
    args_list.append(arg)

save_to_json_file(args_list, filename)