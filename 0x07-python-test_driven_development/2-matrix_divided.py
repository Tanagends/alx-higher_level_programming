#!/usr/bin/python3
"""Module for diving a Matrix"""

def matrix_divided(matrix, div):
    """Divides a matrix by a number"""

    new = [[el for el in ro] for ro in matrix]
    if not isinstance(div, float) and not isinstance(div, int):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    length = -1
    for i, row in enumerate(matrix):
        if length != len(row) and length != -1:
            raise TypeError("Each row of the matrix must have the same size")
        length =  len(row)
        for j, element in enumerate(row):
            if not isinstance(element, float) and not isinstance(element, int):
                raise TypeError("matrix must be a matrix (list of lists)\
                of integers/floats")
            new[i][j] = round((element / div), 2)
    return new
