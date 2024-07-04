#!/bin/bash
# Takes in a URL, sends a DELETE request to that URL
curl -s -X DELETE "http://$1"
