#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last = number % 10
else:
    last = -1 * ((-1 * number) % 10)
print(f"Last digit of {number:d} is {last:d} and is ", end="")
if last == 0:
    print("0")
elif last > 5:
    print("greater than 5")
elif last < 6:
    print("less than 6 and not 0")
