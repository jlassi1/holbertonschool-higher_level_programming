#!/usr/bin/python3
"""  Problem solve """
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get(
        'https://api.github.com/repos/{}/{}/commits'
        .format(argv[2], argv[1]))
    data = r.json()
    try:
        for i in range(10):
            name = data[i].get("commit").get("author").get("name")
            id = data[i].get("sha")
            print("{}: {}".format(id, name))
    Exception:
        pass
