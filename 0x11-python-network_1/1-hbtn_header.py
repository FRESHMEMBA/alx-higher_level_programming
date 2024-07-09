#!/usr/bin/python3
import sys
import urllib.request

with urllib.request.urlopen(sys.argv[1]) as response:
    headers = response.getheaders()
    print(dict(headers).get("X-Request-Id"))
