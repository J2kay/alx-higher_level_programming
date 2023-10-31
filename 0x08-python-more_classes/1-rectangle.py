#!/usr/bin/python3
"""This is a hash bang for a python script"""


class Rectangle:
    """This is a class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """This method retrieves the width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the width property"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This method retrieves the height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height property"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
