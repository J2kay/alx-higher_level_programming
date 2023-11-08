#!/usr/bin/python3
"""a script that adds all arguments to a Python list,
    and then save them to a file"""


import sys
save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
load_from_json_file = __import__
('6-load_from_json_file.py').load_from_json_file

my_args = list(sys.argv[1:])

try:
    data1 = load_from_json_file('add_item.json')
except Exception:
    data1 = []

data1.extend(my_args)
save_to_json_file(data1, 'add_item.json')
