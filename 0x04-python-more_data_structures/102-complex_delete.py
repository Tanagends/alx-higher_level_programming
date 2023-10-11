#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    diction = dict(filter(lambda dictionary: dictionary[1] != value, a_dictionary.items()))
    a_dictionary.clear()
    a_dictionary.update(diction)
    return a_dictionary
a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}
new_dict = complex_delete(a_dictionary, 'C')
print(a_dictionary)
print("--")
print(new_dict)

print("--")
print("--")
new_dict = complex_delete(a_dictionary, 'c_is_fun')
print(a_dictionary)
print("--")
print(new_dict)
