"""CSCA08: Fall 2022 -- Assignment 1: What's that Phrase?

This code is provided solely for the personal and private use of
students taking the CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2020-2022 Mario Badr, Jennifer Campbell, Tom Fairgrieve,
Diane Horton, Michael Liut, Jacqueline Smith, and Anya Tafliovich.

"""

from constants import (POINTS_PER_GUESS, COST_OF_VOWEL, BONUS_POINTS,
                       PLAYER_ONE, PLAYER_TWO, GUESS, BUY, SOLVE,
                       QUIT, SINGLE_PLAYER, PVP, PVE, EASY, HARD,
                       ALL_CONSONANTS, ALL_VOWELS,
                       PRIORITY_CONSONANTS, MYSTERY_CHAR)


# This function is provided as an example.
def winning(mystery_phrase: str, view: str) -> bool:
    """Return True if and only if mystery_phrase and view are a winning
    combination. That is, if and only if mystery_phrase and view are
    the same.

    >>> winning('banana', 'banana')
    True
    >>> winning('apple', 'a^^le')
    False
    >>> winning('apple', 'app')
    False

    """

    return mystery_phrase == view


# This function is partially provided as an example of calling another
# function as helper.
def game_over(mystery_phrase: str, view: str, move: str) -> bool:
    """Return True if and only if mystery_phrase and view are a winning
    combination or move is QUIT.

    """

    return move == QUIT or winning(mystery_phrase, view)


# This function is partially provided as an example of using constants
# in the docstring description and specific values in docstring
# examples.
def is_player(current_player: str, game_type: str) -> bool:
    """Return True if and only if current_player represents a human player
    in a game of type game_type.

    current_player is PLAYER_ONE or PLAYER_TWO.
    game_type is SINGLE_PLAYER, PVP, or PVE.

    In a SINGLE_PLAYER game or a PVP game, a player is always a human
    player. In a PVE game, PLAYER_ONE is a human player and PLAYER_TWO
    is the environment.

    >>> is_player('Player One', 'SP')
    True
    >>> is_player('Player Two', 'PVE')
    False

    """

    pass


# This function is provided as a helper for one of the required functions.
def half_solved(view: str) -> bool:
    """Return True if and only if at least half of the alphabetic
    characters in view are revealed.

    >>> half_solved('')
    True
    >>> half_solved('x')
    True
    >>> half_solved('^')
    False
    >>> half_solved('a^,^c!')
    True
    >>> half_solved('a^b^^e ^c^d^^d')
    False
    """

    num_mystery_chars = view.count(MYSTERY_CHAR)
    num_alphabetic = 0
    for char in view:
        if char.isalpha():
            num_alphabetic += 1
    return num_alphabetic >= num_mystery_chars


if __name__ == '__main__':
    import doctest
    doctest.testmod()
