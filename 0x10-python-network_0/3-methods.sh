#!/bin/bash
# Takes in a URL, and displays all the HTTP methods the server will accept
curl -s -I -X OPTIONS "http://$1" | grep "Allow:" | awk '{print $2'}
