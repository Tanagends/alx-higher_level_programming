#!/usr/bin/python3

from sys import argv

def main():
    l = len(argv)
    sum = 0
    for i in range(1, l):
        sum += int(argv[i])
    print("{0:d}".format(sum))

if __name__ == "__main__":
    main()
