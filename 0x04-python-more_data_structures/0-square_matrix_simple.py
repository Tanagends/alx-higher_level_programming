#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    mat = matrix.copy()
    for row in mat:
        row[:] = list(map(lambda x: x ** 2, row))
    return mat
