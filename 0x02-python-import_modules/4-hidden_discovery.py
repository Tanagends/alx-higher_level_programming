#!/usr/bin/python3

import imp


if __name__ == "__main__":
    module = imp.load_compiled("hidden", "hidden_4.pyc")
    li = dir(module)
    li.sort()
    for element in li:
        if not element.startswith("_"):
            print(element)
