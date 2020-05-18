#!/usr/bin/python3
def safe_print_integer_err(value):
    from sys import stderr
    try:
        print("{:d}".format(value))
        return True
    except ValueError as err:
        stderr.write("Exception: {}\n".format(err))
        return False
