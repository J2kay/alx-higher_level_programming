#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return None
    new_list = set(my_list)
    result = sum(new_list)
    return result
