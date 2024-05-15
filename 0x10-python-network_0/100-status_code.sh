#!/bin/bash
# Takes in a URL, sends a request to that URL
curl -s -o dev/null -w "%{http_code}\n" "http://$1"
