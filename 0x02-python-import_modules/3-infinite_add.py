#!/usr/bin/python3
from sys import argv
x = 0
if __name__ == '__main__':
    for i in range(1, len(argv)):
        x += int(argv[i])

    print("{:d}".format(x))
