"""Week 3 worksheet problems: sample solutions."""


def same_abs(num1: float, num2: float) -> bool:
    """Return whether num1 and num2 have the same absolute value.

    >>> same_abs(-3.2, 3.2)
    True
    >>> same_abs(3.0, 3.5)
    False

    """

    return abs(num1) == abs(num2)


def is_isosceles_triangle(side1: int, side2: int, side3: int) -> bool:
    """Return whether a triangle with side lengths side1, side2, and side3
    is isosceles.

    Precondition: side1, side2, and side3 are valid side lengths of a
                  triangle.

    >>> is_isosceles_triangle(3, 4, 5)
    False
    >>> is_isosceles_triangle(3, 3, 5)
    True
    >>> is_isosceles_triangle(3, 5, 3)
    True
    """

    return side1 == side2 or side2 == side3 or side1 == side3


def is_right_triangle(side1: int, side2: int, hypotenuse: int) -> bool:
    """Return whether a triangle with sides of length side1 and side2, and
    hypotenuse of length hypotenuse is a right triangle.

    Precondition: side1, side2, and side3 are valid side lengths of a
                  triangle.

    >>> is_right_triangle(3, 4, 5)
    True
    >>> is_right_triangle(2, 2, 4)
    False

    """

    return side1 ** 2 + side2 ** 2 == hypotenuse ** 2


if __name__ == '__main__':
    import doctest
    doctest.testmod()
