#!/usr/bin/python3
"""a class MyList that inherits from list"""


class MyList(list):
    """a class MyList that inherits from list"""
    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        my_list = sorted(self)
        print(my_list)
