#!/usr/bin/bash
# Takes in a URL, sends a request to that URL,
# and displays the response's body size 
URL=$1
curl -s -w "%{size_download}\n"