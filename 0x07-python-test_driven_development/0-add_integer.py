#!/usr/bin/python3
"""This is a python hash bang"""


def add_integer(a, b=98):
    """This functions returns the sum of two integers or floats"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a1 = int(a) if isinstance(a, float) else a
    b1 = int(b) if isinstance(b, float) else b

    return a1 + b1
