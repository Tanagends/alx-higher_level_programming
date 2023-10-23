#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except TypeError:
            pass
        except IndexError:
            print()
            return count
    print()
    return count

print(safe_print_list([1, 2, 3], 7))
