#!/usr/bin/python3
for i in range(100):
    if i < 10:
        print("{0}{1}".format(0, i), end=", ")
    else:
        print("{0}".format(i), end=", " if i != 99 else "\n")
