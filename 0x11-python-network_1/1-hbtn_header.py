#!/usr/bin/python3

"""
takes in a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response.
"""

import sys
import urllib.request

with urllib.request.urlopen(sys.argv[1]) as response:
    headers = response.getheaders()
    print(dict(headers).get("X-Request-Id"))