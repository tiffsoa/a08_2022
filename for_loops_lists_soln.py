"""Solutions to the worksheet on for loops and lists.
"""


def collect_underperformers(nums: list[int], threshold: int) -> list[int]:
    """Return a new list consisting of those numbers in nums that are below
    threshold, in the same order as in nums.

    >>> collect_underperformers([1, 2, 3, 4], 3)
    [1, 2]
    >>> collect_underperformers([1, 2, 100, 3, 4], 50)
    [1, 2, 3, 4]
    >>> collect_underperformers([], 7)
    []
    >>> collect_underperformers([8, 9, 10], 7)
    []
    """

    # the accumulator variable; this is a NEW list object
    underperformers = []

    for item in nums:
        if item < threshold:
            underperformers.append(item)

    # Return the new list object. The list nums is not changed.
    return underperformers


def scale_midterm_grades(grades: list[int], multiplier: int,
                         bonus: int) -> None:
    """Modify grades by multiplying each item by multiplier and then
    adding bonus. Cap grades at 100.

    >>> grades = [45, 50, 55, 95]
    >>> scale_midterm_grades(grades, 1, 10)
    >>> grades
    [55, 60, 65, 100]
    >>> grades = []
    >>> scale_midterm_grades(grades, 42, 42)
    >>> grades
    []
    """

    for i in range(len(grades)):
        grades[i] = min(grades[i] * multiplier + bonus, 100)
    # No new list is created. The input list grades is modified.
    # There is no return statement: the function returns None.

    # This does not work. Can you see why?
    # for grade in grades:
    #    grade = min(grade * multiplier + bonus, 100)

    # This does not work either. Can you see why?
    # new_grades = []
    # for grade in grades:
    #     new_grades.append(min(grade * multiplier + bonus, 100))
    # grades = new_grades


if __name__ == '__main__':

    import doctest
    doctest.testmod()
