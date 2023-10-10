#!/usr/bin/python3
def no_c(my_string):
    new_str = [i for i in my_string if i != 'c' and i != 'C']
    n_str = "".join(new_str)
    return n_str
