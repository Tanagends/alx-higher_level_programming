#!/usr/bin/python3

from calculator_1 import add, mul, sub, div
import sys


if __name__ == "__main__":
    if len(argv != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if argv[2] not in "+-/*":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(argv[1])
    b = int(argv[3])
    match(argv[2]):
        case "+":
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        case "-":
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        case "/":
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
        case "*":
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
