#!/usr/bin/python3
"""Creates a pascal triangle as a list of lists"""


def pascal_triangle(n):
    """returns a list of int listsrepresenting a pascal triangle"""
    if n <= 0:
        return []

    pascal_list = []

    for i in range(n):
        match i:
            case 0:
                pascal_list.append([1])
                continue
            case 1:
                pascal_list.append([1, 1])
                continue
            case _:
                pass
        row = [1]
        row.extend(list(map((lambda x, y: x + y),
        pascal_list[-1], pascal_list[-1][1:])))
        row.append(1)
        pascal_list.append(row)

    return pascal_list
