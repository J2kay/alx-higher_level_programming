#!/usr/bin/python3
"""This function prints all the attributes and methods"""


def lookup(obj):
    """
    This function returns a list of
    available attributes and methods of an object
    """
    my_list = []
    my_list = dir(obj)
    return my_list
