#!/bin/bash
# Takes in a URL, and displays all the HTTP methods the server will accept
curl -s -I -L -X OPTIONS "http://$1"
