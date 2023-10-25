#!/usr/bin/python3
"""This is a hash bang header"""


class Square:
    """This is a class that defines a square"""

    def __init__(self, size=0):
        """This method initializes the object with the specified
            values for parameter1.
            It sets these values as instance variables for the object"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
