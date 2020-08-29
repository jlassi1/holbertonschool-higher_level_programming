#!/usr/bin/python3
"""  A script that fetches URL """
import requests
import sys


if __name__ == "__main__":

    pram = {'q': ""}
    if len(sys.argv) == 2:
        pram['q'] = sys.argv[1]

    r = requests.post('http://0.0.0.0:5000/search_user', data=pram)
    try:
        if not r.json():
            print("No result")
        else:
            print("[{}] {}".format(r.json().get('id'), r.json().get('name')))
    except ValueError:
        print('Not a valid JSON')
