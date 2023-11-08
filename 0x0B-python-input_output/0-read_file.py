#!/usr/bin/python3
"""a function that reads a text file"""


def read_file(filename=""):
    """a function that reads a text file"""
    with open(filename, encoding='utf-8') as f:
        data_read = f.read
