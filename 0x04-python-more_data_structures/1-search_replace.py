#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list:
        return None
    list_copy = my_list.copy()
    check = False
    for i in range(len(list_copy)):
        if list_copy[i] == search:
            list_copy[i] = replace
            check = True
    if not check:
        return None
    return list_copy
