#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    roman_list = list(roman.keys())
    val_list = []
    if not roman_string or roman_string not str:
        return 0
    for char in roman_string:
        if char not in roman_list:
            continue
        val_list.append(roman[char])
    for i in range(len(val_list) - 1):
        if val_list[i] < val_list[i + 1]:
            val_list[i] = -val_list[i]
    return sum(val_list)
