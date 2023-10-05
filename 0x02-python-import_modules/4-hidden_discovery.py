#!/usr/bin/python3

import hidden_4


if __name__ == "__main__":
    li = dir(hidden_4)
    li.sort()
    for element in li:
        if not element.startswith("_"):
            print(element)
