#!/usr/bin/python3
"""This class inherits from int"""


class MyInt(int):
    """
    MyInt is a rebel. MyInt has == and != operators inverted
    """
    def __new__(cls, *args, **kwargs):
        """creates anew instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """now not equal"""
        return int(self) != other

    def __ne__(self, other):
        """now equal"""
        return int(self) == other
