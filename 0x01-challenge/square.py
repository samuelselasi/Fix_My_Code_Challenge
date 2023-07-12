#!/usr/bin/python3
"""Python module to calculate perimeter and area of a square"""


class Square():
    """Class that calculates area and perimeter of a Square"""
    def __init__(self, width: int = 0, height: int = 0, **kwargs):
        """Function that initializes instances"""
        self.width = width
        self.height = height
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self) -> int:
        """ Area of the square """
        return (self.width * self.height)

    def perimeter_of_my_square(self) -> int:
        """Perimeter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self) -> str:
        """Print instances"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """Creates square"""
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
