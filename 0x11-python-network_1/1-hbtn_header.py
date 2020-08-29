#!/usr/bin/python3
""" A script that fetches URL  """
import urllib.request
import sys


rep = urllib.request.Request(sys.argv[1])
with urllib.request.urlopen(rep) as rsp:
    print(rsp.getheader('X-Request-Id'))
