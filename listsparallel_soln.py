"""Sample solutions to the worksheet on parallel lists and strings.
"""


def stretch_string(text: str, stretch_factors: list[int]) -> str:
    """Return a string consisting of the characters in text in the same
    order as in text, repeated the number of times indicated by the
    item at the corresponding position of stretch_factors.

    Precondition: len(text) == len(stretch_factors) and the items of
                  stretch_factors are non-negative

    >>> stretch_string('Hello', [2, 0, 3, 1, 1])
    'HHllllo'
    >>> stretch_string('echo', [0, 0, 1, 5])
    'hooooo'
    >>> stretch_string('', [])
    ''
    >>> stretch_string('x', [5])
    'xxxxx'
    >>> stretch_string('x', [0])
    ''
    >>> stretch_string('math', [0, 0, 0, 0])
    ''
    >>> stretch_string('math', [1, 1, 1, 1])
    'math'

    """

    result = ''
    for i in range(len(text)):
        result = result + text[i] * stretch_factors[i]

    return result


def greatest_difference(nums1: list[int], nums2: list[int]) -> int:
    """Return the greatest absolute difference between numbers at corresponding
    positions in nums1 and nums2.

    Precondition: len(nums1) == len(nums2) > 0

    >>> greatest_difference([1, 2, 3], [6, 8, 10])
    7
    >>> greatest_difference([1, -2, 3], [-6, 8, 10])
    10
    >>> greatest_difference([1], [1])
    0
    >>> greatest_difference([-1], [-5])
    4
    >>> greatest_difference([1, 2, 3], [1, 2, 3])
    0
    """

    # Try 1:
    # build a list of differences, then take max.
    # diffs = []
    # for i in range(len(nums1)):
    #     diffs.append(abs(nums1[i] - nums2[i]))
    # return max(diffs)

    # Problems: two traverslas instead of one: once to build the list
    # and once to find the max; list needs to be stored in memory.

    # max_diff = 0
    # for i in range(len(nums1)):
    #     diff = abs(nums1[i] - nums2[i])
    #     if diff > max_diff:
    #         max_diff = diff
    # return max_diff

    # OR:
    max_diff = 0
    for i in range(len(nums1)):
        max_diff = max(max_diff, abs(nums1[i] - nums2[i]))
    return max_diff


if __name__ == '__main__':

    import doctest
    doctest.testmod()
