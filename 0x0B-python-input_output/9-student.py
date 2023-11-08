#!/usr/bin/python3
"""contains the class student"""


class Student:
    """defines a student"""
    def __init__(self, first_name, last_name, age):
        """initializes values"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """"returns dictionary representation of Student"""
        return self.__dict__
