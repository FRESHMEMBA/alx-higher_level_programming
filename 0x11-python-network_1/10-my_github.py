#!/usr/bin/python3


"""
Takes GitHub credentials and uses the GitHub API
to display the (user) id
"""


import sys
import requests
import requests.auth


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"

    response = requests.get(
        url=url,
        auth=requests.auth.HTTPBasicAuth(
            username=username,
            password=password
            )
        )

    if response.status_code == 200:
        print(response.json().get("id"))
    else:
        print("None")
