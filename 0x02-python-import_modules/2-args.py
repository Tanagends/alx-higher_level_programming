#!/usr/bin/python3

from sys import argv


def main():
    length = len(argv) - 1
    if length == 0:
        print("{0:d} arguments.".format(length))
    elif length == 1:
        print("{0:d} argument:".format(length))
    else:
        print("{0:d} arguments:".format(length))
    for i in range(1, length + 1):
        print("{0}: {1}".format(i, argv[i]))


if __name__ == "__main__":
    main()
