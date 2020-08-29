#!/usr/bin/python3
# a Python script that fetches https://intranet.hbtn.io/status
""" A script that fetches URL  """
import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    the_page = response.read()
    print('Body response:')
    print("\t- type: {}".format(type(the_page)))
    print("\t- content: {}".format(the_page))
    print("\t- utf8 content: {}".format(the_page.decode('utf-8')))
