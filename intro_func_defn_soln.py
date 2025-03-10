"""Code for week 2 worksheets: sample solutions.
"""

# Terminology!

# function header: the very first line, begins with def: line 14 for
#                  function add_bonus
# function name: add_bonus
# parameters: grade, bonus
# parameter types: float, float
# return type: float (after the symbol ->)
# docstring: between the triple quotes immediately after the header
# function body: the code except for the header, immediately after the
#                docstring
# arguments: the actual values in the function call;
#            for example, 67.0 and 10.0


def add_bonus(grade: float, bonus: float) -> float:
    """Return the result of adding the bonus bonus to a grade grade,
    capped at 100.0.

    >>> add_bonus(67.0, 10.0)
    77.0
    >>> add_bonus(92.5, 9.0)
    100.0

    """

    return min(100.0, grade + bonus)


def percentage(num: int, out_of: int) -> int:
    """Return what percent num is of out_of, rounded to an int, using the
    function round for rounding.

    >>> percentage(10, 200)
    5
    >>> percentage(151, 300)
    50

    """

    # Compare with these! They all produce different results:
    # return int(num / out_of * 100)
    # return num // out_of * 100
    # return num * 100 // out_of
    # return round(num / out_of) * 100

    return round(num / out_of * 100)


def max_of_min(num1: float, num2: float, val1: float, val2: float) -> float:
    """Return the maximum of the minimums of the pairs num1 and num2, and
    val1 and val2.

    >>> max_of_min(4.0, 3.7, 6.0, 3.5)
    3.7
    >>> max_of_min(1.0, 1.7, 4.5, 3.0)
    3.0

    """

    # min_nums = min(num1, num2)
    # min_vals = min(val1, val2)
    # return max(min_nums, min_vals)
    # or, alternatively (both are equally good solutions):

    return max(min(num1, num2), min(val1, val2))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
