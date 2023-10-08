#!/usr/bin/python3
def no_c(my_string):
    str_list = []
    for char in my_string:
        if char not in "cC":
            str_list.append(char)
    return "".join(str_list)
