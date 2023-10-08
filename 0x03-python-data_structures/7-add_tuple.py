#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lena = len(tuple_a)
    lenb = len(tuple_b)

    if lena >= 2 and lenb >= 2:
        a, b = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    if lena == 1:
        a_copy = (tuple_a[0], 0)
    elif lena == 0:
        a_copy = (0, 0)
    else:
        a_copy = tuple_a[:]

    if lenb == 1:
        b_copy = (tuple_b[0], 0)
    elif lenb == 0:
        b_copy = (0, 0)
    else:
        b_copy = tuple_b[:]

    result = (a_copy[0] + b_copy[0], a_copy[1] + b_copy[1])

    return result
