#!/bin/bash
# Takes in a URL, sends a GET request to that URL
curl -s -L -H "X-School-User-Id: 98" "http://$1"
