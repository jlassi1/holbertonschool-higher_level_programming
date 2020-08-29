#!/usr/bin/python3
"""  A script that fetches URL """
import requests
import sys


if __name__ == "__main__":
    pram = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], data=pram)
    print(r.text)
