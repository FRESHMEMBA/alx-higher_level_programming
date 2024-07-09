#!/bin/bash
# Takes in a URL, sends a GET request to that URL
curl -s -L -w "http://$1"
