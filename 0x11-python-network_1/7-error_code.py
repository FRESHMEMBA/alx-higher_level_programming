#!/usr/bin/python3


"""
Takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""


import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = requests.get(url=url)
        print(f"{response.text}")

    except requests.HTTPError as e:
        if int(e.code) >= 400:
            print(f"Error code: {e.code}")
