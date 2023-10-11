#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    add_list = sum(list(map(lambda x: x[0] * x[1], my_list)))
    weight_total = sum(list(map(lambda x: x[1], my_list)))
    return add_list / weight_total
