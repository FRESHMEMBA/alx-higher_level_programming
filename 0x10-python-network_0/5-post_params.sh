#!/bin/bash
# Takes in a URL, sends a DELETE request to that URL
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" -X POST "http://$1"
