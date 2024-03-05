#!/usr/bin/python3
"""
Script to add all command-line arguments to a Python list and
then save them to a JSON file.

This script takes command-line arguments and stores them in a Python list.
It then saves this list to a JSON file for later use.
"""


import sys
import json

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file.py").load_from_json_file


def main():
    """
    Main function to process command-line arguments
    and save to JSON file
    """
    # Define the filename for the JSON file
    filename = "add_item.json"
    args_list = []

    # Extract command-line arguments and add them to the list
    for arg in sys.argv[1:]:
        args_list.append(arg)

    # Save the list of arguments to a JSON file
    save_to_json_file(args_list, filename)


if __name__ == "__main__":
    main()