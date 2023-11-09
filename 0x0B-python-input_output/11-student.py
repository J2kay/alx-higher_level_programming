#!/usr/bin/python3
"""contains the class student"""


class Student:
    """defines a student"""
    def __init__(self, first_name, last_name, age):
        """initializes values"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """"returns dictionary representation of Student"""
        if attrs is None:
            return self.__dict__

        result = {}
        for attr in attrs:
            if hasattr(self, attr):
                result[attr] = getattr(self, attr)
        return result

    def reload_from_json(self, json):
        """Replaces all attributes of the Student"""
        for k, v in json.items():
            setattr(self, k, v)
