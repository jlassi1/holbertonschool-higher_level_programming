#!/usr/bin/python3
"""  A script that fetches URL """
from urllib.error import HTTPError
from urllib.request import Request, urlopen
import sys


if __name__ == "__main__":
    req = Request(sys.argv[1])
    try:
        with urlopen(req) as f:
            print(f.read().decode('utf-8'))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
