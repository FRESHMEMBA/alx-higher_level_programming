#!/usr/bin/python3


"""
Takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""


import sys
import requests


if __name__ == "__main__":
    q = "" if len(sys.argv) == 1 else sys.argv[1]
    url = "http://0.0.0.0:5000/search_user"
    data = {
        "q": q
    }

    try:

        response = requests.post(url=url, data=data)
        response_json = response.json()

        if isinstance(response_json, dict) and response_json:
            print(f"[{response_json['id']}] {response_json['name']}")
        elif isinstance(response_json, list) and not response_json:
            print("No result")
        else:
            print("Not a valid JSON")

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
