"""CSCA08 Files Worksheet: Sample solutions.
"""

from typing import TextIO


def is_correct(dict_file: TextIO, word: str) -> bool:
    """Return True if and only if word is in dict_file.
    Note: current position in dict_file will change as a result of the call.

    Pre: word is not empty
         dict_file is open for reading,
                   current position at the beginning of the file

    >>> with open('dictionary.txt') as dict_file:
    ...     is_correct(dict_file, 'Zyrtec')
    True
    >>> with open('dictionary.txt') as dict_file:
    ...     is_correct(dict_file, 'lolz')
    False
    """

    # lines = file.read()
    # return word in lines  # mistake: what about "Zyr"? or "Zworkykin\nZyrtec"

    # lines = dict_file.readlines()
    # return word in lines  # mistake: forgot about newline characters!

    # lines = dict_file.readlines()
    # return word + '\n' in lines  # works!

    # how long is this list of lines?
    # we don't need to store it!
    # do we need to read the entire file?

    # Early return pattern
    # for line in dict_file:
    #     if word in line:  # mistake: what about "Zyr"?
    #         return True
    # return False

    # Early return pattern
    for line in dict_file:
        if word + '\n' == line:  # or: if word == line[:-1]
            return True
    return False


def write_ascii_triangle(outfile: TextIO, block: str, sidelength: int) -> None:
    """Write an ascii isosceles right triangle using block that is sidelength
    characters wide and high to outfile. The right angle should be in the
    upper-left corner.

    Precondition: len(block) == 1
                  sidelength >= 0
                  outfile is open for writing

    For example, given block="@" and sidelength=4, the following
    should be written to the file:

    @@@@
    @@@
    @@
    @

    """

    # sidelength blocks
    # sidelength - 1 blocks
    # sidelength - 2 blocks
    # ...
    # 1 block

    # for i in range(sidelength, 0, -1):
    #     outfile.write(block * i + '\n')

    # or with a while loop:
    while sidelength > 0:
        outfile.write(block * sidelength + '\n')
        sidelength -= 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    with open('triangle.txt', 'w') as triangle_file:
        write_ascii_triangle(triangle_file, '@', 5)

    with open('triangle2.txt', 'w') as triangle_file_2:
        write_ascii_triangle(triangle_file_2, 'x', 10)
