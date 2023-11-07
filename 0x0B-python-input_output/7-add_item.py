#!/usr/bin/python3
""""Adds all arguments to a python list then adds to file"""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
    
    try:
        file_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        file_list = []
    file_list.extend(sys.argv[1:])
    save_to_json_file(file_list, "add_item.json")
