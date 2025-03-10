"""Code for week 2 worksheets: sample solution.
"""


def format_name(first: str, last: str) -> str:
    """Return the full name of a person with first name first_name and
    last name last_name.  Specifically, return the string in the
    format:
    last_name, first_name
    i.e. last_name followed by comma, followed by space, followed by
    first_name.

    >>> format_name('Anya', 'Tafliovich')
    'Tafliovich, Anya'
    >>> format_name('Ada', 'Lovelace')
    'Lovelace, Ada'

    """

    return last + ', ' + first


def to_listing(first: str, last: str, phone_number: str) -> str:
    """Return the phone book listing of a person with first name first_name,
    last name last_name, and phone number phone_number. Specifically,
    return the string in the format:
    last_name, first_name: phone_number
    i.e. last_name followed by comma, followed by space, followed by
    first_name followed by colon, followed by space, followed by
    phone_number.

    >>> to_listing('Anya', 'Tafliovich', '123-456-7890')
    'Tafliovich, Anya: 123-456-7890'
    >>> to_listing('Ada', 'Lovelace', '010')
    'Lovelace, Ada: 010'

    """

    return format_name(first, last) + ': ' + phone_number

# Homework: trace the line
# listing = to_listing('Ada', 'Lovelace', '010')
# in the visualizer!


if __name__ == '__main__':
    import doctest
    doctest.testmod()
