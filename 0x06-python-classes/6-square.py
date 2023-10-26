#!/usr/bin/python3
"""This is a hash bang header"""


class Square:
    """This is a class that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """This method initializes the object with the specified
            values for parameter1.
            It sets these values as instance variables for the object"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.position = position

    def area(self):
        """This method returns the current square area"""
        return self.__size ** 2

    @property
    def size(self):
        """retrieves the property"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter method for the size property"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be an integer")
        self.__size = value

    def my_print(self):
        """that prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

    @property
    def position(self):
        """retrieves the position property"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for the position property"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(v, int) and v >= 0 for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
