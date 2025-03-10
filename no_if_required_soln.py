"""Week 3 worksheet problems: sample solutions."""


def can_vote(age: int) -> bool:
    """Return whether age is legal voting age of at least 18 years.

    >>> can_vote(16)
    False
    >>> can_vote(21)
    True

    """

    return age >= 18


def is_teenager(age: int) -> bool:
    """Return whether a person who is age years old is a teenager between
    13 and 18 inclusive.

    >>> is_teenager(4)
    False
    >>> is_teenager(16)
    True
    >>> is_teenager(19)
    False
    """

    # return age >= 13 and age <= 18  # in any language
    return 13 <= age <= 18   # in Python


if __name__ == '__main__':
    import doctest
    doctest.testmod()
