#!/usr/bin/python3
"""
    a function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited
    from, the specified class ; otherwise False.
    """


def is_kind_of_class(obj, a_class):
    """
    a function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited
    from, the specified class ; otherwise False.
    """
    new_class = obj.__class__

    while new_class is not None:
        if new_class == a_class:
            return True
        new_class = new_class.__base__
    return False
