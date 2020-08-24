#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept.
curl -X OPTIONS $1 -i | grep "Allow:" | cut -d " " -f 1-4
