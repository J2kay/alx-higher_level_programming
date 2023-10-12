#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list:
        return None
    if not replace:
        return my_list
    list_copy = my_list.copy()
    for i in range(len(list_copy)):
        if list_copy[i] == search:
            list_copy[i] = replace
    return list_copy
