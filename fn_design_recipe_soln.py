"""Code for week 2 worksheets: sample solution.
"""

from math import ceil


def number_of_boxes(num_pencils: int, pencils_per_box: int) -> int:
    """Return the minimum number of boxes needed to pack num_pencils
    pencils, if each box can hold up to pencils_per_box pencils.

    num_pencils >= 0
    pencils_per_box > 0

    >>> number_of_boxes(200, 10)
    20
    >>> number_of_boxes(206, 10)
    21
    >>> number_of_boxes(0, 25)
    0
    >>> number_of_boxes(1, 25)
    1

    """

    return ceil(num_pencils / pencils_per_box)


def calculate_total(bill_amount: float, tax_rate: float) -> float:
    """Return the total amount to be paid on a bill of bill_amount
    dollars, given the tax rate tax_rate.

    bill >= 0
    0 <= tax_rate <= 1

    >>> calculate_total(2.0, 0.13)
    2.26
    >>> calculate_total(0.0, 0.13)
    0.0
    >>> calculate_total(2.0, 1.0)
    4.0

    """

    return bill * (1 + tax_rate)

# Note: Be careful when running docstring exmaples with doctest if the
# return value is a float -- it may fail due to inexact calculation!
# We will learn how to deal with this issue later in the course.


if __name__ == '__main__':
    import doctest
    doctest.testmod()
