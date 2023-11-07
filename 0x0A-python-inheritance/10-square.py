#!/usr/bin/python3
"""
    an empty class BaseGeometry.
    """


class BaseGeometry:
    """
    an empty class BaseGeometry.
    """
    def area(self):
        """
        raises an Exception with the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This method validates the value
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


"""This class defines a Rectangle"""


class Rectangle(BaseGeometry):
    """
    This class defines a rectangle
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ this method returns the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """string representation"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)


"""This class defines a square"""


class Square(Rectangle):
    """ A subclass of Rectangle"""
    def __init__(self, size):
        """Constructor"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """rreturns the area of a square"""
        return self.__size ** 2
