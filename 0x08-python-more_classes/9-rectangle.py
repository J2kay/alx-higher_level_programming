#!/usr/bin/python3
"""This is a hash bang for a python script"""


class Rectangle:
    """This is a class that defines a rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """This method returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """This metho returns the perimeter of the rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """string representation of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""

        if isinstance(self.print_symbol, str):
            print_symbol = self.print_symbol
        elif isinstance(self.print_symbol, list):
            print_symbol = self.print_symbol[0]
        else:
            print_symbol = "#"

        rectangle_str = ""
        for i in range(self.height):
            rectangle_str += print_symbol * self.width + "\n"
        return rectangle_str[:-1]

    def __repr__(self):
        """This returns a representation of the class"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """This built-in methods performs clean_up actions"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """This method returns the biggest rectangle based on the are"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.width * rect_1.height
        area_2 = rect_2.width * rect_2.height

        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size"""
        return cls(size, size)
