#!/usr/bin/python3
""""Adds all arguments to a python list then adds to file"""
import sys
import json
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

file_list = load_from_json_file(add_item.json)
save_to_json_file(file_list.extend(sys.argv[1:]), add_item.json)
