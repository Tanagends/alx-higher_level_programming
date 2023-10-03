#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        last = ((number * -1) % 10) * -1
    else:
        last = number % 10
        print("{0}".format(last), end="")
        return last
result = print_last_digit(88)
print(result)
