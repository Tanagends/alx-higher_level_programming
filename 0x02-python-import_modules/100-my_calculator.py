#!/usr/bin/python3

from calculator_1 import add, mul, sub, div
import sys


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if sys.argv[2] not in "+-/*":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = (sys.argv[2]):
    if operator == "+":
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif operator == "-":
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif operator == "/":
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
    elif operator == "*":
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
