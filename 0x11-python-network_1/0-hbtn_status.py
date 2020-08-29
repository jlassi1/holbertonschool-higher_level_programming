#!/usr/bin/python3
# a Python script that fetches https://intranet.hbtn.io/status
""" A script that fetches URL  """
import urllib.request


the_page = ""
#req = urllib.request.Request('https://intranet.hbtn.io/status')
with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    the_page += "-" + str(response.read())

print(the_page)
