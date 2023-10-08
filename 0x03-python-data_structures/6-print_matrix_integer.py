#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for number in row:
            print("{:d}".format(number), end= " " 
                    if number != row[-1] else "")
        print()
matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
print_matrix_integer(matrix)
