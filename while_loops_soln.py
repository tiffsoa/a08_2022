"""Worksheet on While Loops: sample solution."""


def every_nth_character(text: str, n: int) -> str:
    """Return a string containing every nth character from text, starting
    at index 0.

    Precondition: n > 0

    >>> every_nth_character('Computer Science', 3)
    'CpeSee'
    >>> every_nth_character('Computer Science', 1)
    'Computer Science'
    >>> every_nth_character('', 42)
    ''
    >>> every_nth_character('x', 4)
    'x'
    >>> every_nth_character('CSCA08', 10)
    'C'

    """

    result = ''    # an accumulator variable!
    i = 0

    # careful: saying i <= len(text) will result in an error!
    while i < len(text):
        result = result + text[i]
        i = i + n

    return result


def find_letter_n_times(text: str, letter: str, n: int) -> str:
    """Return the shortest substring of text starting from index 0 that
    contains n occurrences of letter.

    Precondition: letter occurs at least n times in text
                  n >= 0
                  len(letter) == 1

    >>> find_letter_n_times('Computer Science', 'e', 2)
    'Computer Scie'
    >>> find_letter_n_times('Computer Science', 'e', 3)
    'Computer Science'
    >>> find_letter_n_times('Computer Science', 'e', 0)
    ''
    >>> find_letter_n_times('', 'x', 0)
    ''
    >>> find_letter_n_times('x', 'x', 1)
    'x'
    >>> find_letter_n_times('x', 'x', 0)
    ''

    """

    i = 0
    count = 0

    # without precondition, this is not safe, need i < len(text) and count < n
    # with precondition, this is better, since no unnecessary check
    while count < n:
        if text[i] == letter:
            count = count + 1
        i = i + 1

    return text[:i]  # think: why not text[:i + 1]?


def count_collatz_steps(n: int) -> int:
    """Return the number of steps it takes to reach 1 by applying the two
    rules of the Collatz conjecture beginning from n.

    Precondition: n >= 1

    >>> count_collatz_steps(6)
    8
    >>> count_collatz_steps(1)
    0
    >>> count_collatz_steps(2)
    1
    >>> count_collatz_steps(3)
    7
    """

    steps = 0

    while n > 1:  # or n != 1
        # make one Collatz step:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        steps = steps + 1

    return steps


def index_of_first_digit(text: str) -> int:
    """Return the index of the first digit character in text, or len(text)
    if there is no digit character in text.

    >>> index_of_first_digit('')
    0
    >>> index_of_first_digit('1')
    0
    >>> index_of_first_digit('x')
    1
    >>> index_of_first_digit('abracadabra')
    11
    >>> index_of_first_digit('abra123cadabra123')
    4
    >>> index_of_first_digit('2abracadabra')
    0

    """

    i = 0

    while i < len(text) and text[i] not in '0123456789':
        i = i + 1
    return i


if __name__ == '__main__':
    import doctest
    doctest.testmod()
