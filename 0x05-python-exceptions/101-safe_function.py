#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        res = fct(*args)
    except Exception as err:
        print("Exception: {}".format(err), file=stderr)
        return None
    else:
        return res
