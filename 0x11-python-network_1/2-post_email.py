#!/usr/bin/python3
""" A script that fetches URL """
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":

    myobj = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(myobj)
    data = data.encode('ascii')

    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as f:
        print(f.read().decode('utf-8'))
