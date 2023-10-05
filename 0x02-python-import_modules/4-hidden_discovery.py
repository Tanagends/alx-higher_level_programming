#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":
    li = dir().sort()
    for element in li:
        if element.startswith("_") == False:
            print(element)
