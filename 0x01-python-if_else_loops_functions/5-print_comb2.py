#!/usr/bin/python3
for i in range(100):
    if i < 10:
        print(0, i, sep="", end=", ")
    else:
        print("{0}".format(i), end=", " if i != 99 else "\n")

