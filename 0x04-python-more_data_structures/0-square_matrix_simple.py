#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return []
    mat = []
    for row in matrix:
        mat.append(list(map(lambda x: x ** 2, row)))
    return mat
