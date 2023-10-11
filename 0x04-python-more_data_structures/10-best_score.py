#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    value = max(list(a_dictionary.values()))
    pair = list(filter(lambda key: a_dictionary[key] == value, a_dictionary))
    return pair[0] if pair else None
