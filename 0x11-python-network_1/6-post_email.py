#!/usr/bin/python3


"""
Takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the
response (decoded in utf-8)
"""


import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {
        "email": email,
    }

    # make a post request to the server
    response = requests.post(url=url, data=data)

    # print the body response
    print(f"{response.text}")
