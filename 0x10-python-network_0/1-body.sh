#!/bin/bash
# Takes in a URL, sends a request to that URL
curl -s -w "%{size_download}\n" -o /dev/null "http://$1"