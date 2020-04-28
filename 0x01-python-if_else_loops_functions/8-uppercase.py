#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            x = ord(c) - 32
        else:
            x = ord(c)
        print("{:c}".format(x), end="")
    print()
