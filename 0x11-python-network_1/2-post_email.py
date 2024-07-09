#!/usr/bin/python3


"""
Takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the
response (decoded in utf-8)
"""


import sys
from urllib import request, parse


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {
        "email": email
    }

    # Encode the data
    encoded_data = parse.urlencode(data).encode("utf-8")

    # Make a request
    req = request.Request(url=url, data=encoded_data)

    with request.urlopen(req) as response:
        body = response.read().decode("utf-8")
        print(f"Your email is: {body}")
