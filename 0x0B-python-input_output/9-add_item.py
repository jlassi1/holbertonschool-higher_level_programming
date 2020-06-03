#!/usr/bin/python3
"""module"""
from sys import argv
save = __import__("7-save_to_json_file").save_to_json_file
load = __import__("8-load_from_json_file").load_from_json_file


try:
    txt = load("add_item.json")
except Exception:
    txt = []

txt += argv[1:]

save(txt, "add_item.json")
