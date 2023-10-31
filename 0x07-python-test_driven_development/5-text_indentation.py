#!/usr/bin/python3
def text_indentation(text):
    """Prints text wiith indentation"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    copy = text[:]

    for delim in ".:?":
        copy_list = copy.split(delim)

        copy = ""
        for item in copy_list:
            item = item.strip(" ")
            copy = item + delim if copy is "" else copy + "\n\n" + item + delim
    print(copy[:-3], end="")
