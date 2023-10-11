#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list:
        return None
    return [item if search != item else replace for item in my_list]
