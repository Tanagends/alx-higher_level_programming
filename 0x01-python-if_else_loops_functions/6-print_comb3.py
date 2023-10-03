#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i < j:
            print("{0}{1}".format(i, j), end="\n" \
                 if i == 8 and j == 9 else ", ")
