#!/bin/bash
# Takes in a URL, sends a request to that URL
curl -s -L -w "%{http_code}\n" "http://$1"
