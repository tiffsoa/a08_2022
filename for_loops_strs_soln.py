'''Worksheet week 4 solutions.'''


def count_uppercase(text: str) -> int:
    """Return the number of uppercase letters in text.

    >>> count_uppercase('BBAManageMenT')
    6
    >>> count_uppercase('abracadabra')
    0
    >>> count_uppercase('')
    0
    """

    count = 0  # accumulator variable
    for character in text:
        if character.isupper():
            count += 1  # short for count = count + 1
    return count


def all_fluffy(text: str) -> bool:
    """Return True iff every character in text is fluffy. Fluffy
    characters are those that appear in the word 'fluffy'. Return True
    if text is empty.

    >>> all_fluffy('')
    True
    >>> all_fluffy('fluffyflu')
    True
    >>> all_fluffy('fluffyxyz')
    False
    >>> all_fluffy('FLUFFYFLU')
    False
    """

    # When do I know the answer?
    # (i)  I see a non-fluffy character (then the answer is False)
    # (ii) I have checked all characters, and they are all fluffy
    #      (then the answer is True)

    for character in text:
        if character not in 'fluy':  # same as not (character in 'fluy')
            return False
    return True


def add_underscores(text: str) -> str:
    """Return a string that contains the characters from text with an
    underscore added after every character except the last.

    >>> add_underscores('Hello')
    'H_e_l_l_o'
    >>> add_underscores('')
    ''
    >>> add_underscores('H')
    'H'

    """

    result = ''

    for character in text:
        result = result + character + '_'

    return result[:-1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
