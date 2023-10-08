#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for number in row:
            print("{:d}".format(number), end=" "
                  if number != row[-1] else "")
        print()
