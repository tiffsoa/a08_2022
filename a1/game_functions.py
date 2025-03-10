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
    """Return True iff mystery_phrase and view are a winning combination or
    move is QUIT.

    Preconditions: view is a valid view for the mystery phrase and move is a
    valid game move.

    >>> game_over('wagon', 'wagon', GUESS)
    True
    >>> game_over('smile', 's^^le', QUIT)
    True
    >>> game_over('madagascar', 'mada', GUESS)
    False
    >>> game_over('harry', 'har', BUY)
    False
    """
    return move == QUIT or winning(mystery_phrase, view)


# This function is partially provided as an example of using constants
# in the docstring description and specific values in docstring
# examples.
def is_player(current_player: str, game_type: str) -> bool:
    """Return True if and only if current_player represents a human player
    in a game of type game_type.

    Preconditions: current_player is a valid player and game_type is a valid
    game type.

    current_player is PLAYER_ONE or PLAYER_TWO.
    game_type is SINGLE_PLAYER, PVP, or PVE.

    In a SINGLE_PLAYER game or a PVP game, a player is always a human
    player. In a PVE game, PLAYER_ONE is a human player and PLAYER_TWO
    is the environment.

    >>> is_player(PLAYER_ONE, SINGLE_PLAYER)
    True
    >>> is_player(PLAYER_TWO, PVE)
    False
    >>> is_player(PLAYER_TWO, PVP)
    True
    >>> is_player(PLAYER_ONE, PVE)
    True
    """
    return current_player == PLAYER_ONE or (current_player == PLAYER_TWO
                                            and game_type != PVE)

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


def one_player(game_type: str) -> bool:

    """Return True if and only if the selected game_type is SINGLE_PLAYER.
    game_type can be SINGLE_PLAYER, PVP, or PVE.

    Preconditions: game_type has to be a valid game type.

    >>> one_player(SINGLE_PLAYER)
    True
    >>> one_player(PVP)
    False
    >>> one_player(PVE)
    False
    """
    return game_type == SINGLE_PLAYER


def current_player_score(player_one_score: int, player_two_score: int,
                         current_player: str) -> int:

    """Return the score of the current player given the score of the first
    player player_one_score and the score of the second one player_two_score.

    Preconditions: current_player is a valid player.

    >>> current_player_score(3, 4, PLAYER_ONE)
    3
    >>> current_player_score(2, 5, PLAYER_ONE)
    2
    >>> current_player_score(4, 6, PLAYER_TWO)
    6
    >>> current_player_score(3, 8, PLAYER_TWO)
    8
    """
    if current_player == PLAYER_ONE:
        return player_one_score
    return player_two_score


def adds_points(given_letter: str, mystery_phrase: str, view: str) -> bool:

    """Return True if and only if the letter in given_letter is a consonant
    displayed as a mystery character.

    Preconditions: view is valid for mystery_phrase and given_letter is
    one character long.

    >>> adds_points('a', 'banana', 'b^^a^a')
    False
    >>> adds_points('r', 'recall', '^ec^^l')
    True
    >>> adds_points('l', 'sociological', '^oc^^^ogi^^^')
    True
    >>> adds_points('n', 'canada', 'c^n^^a')
    False
    """
    return given_letter in mystery_phrase and given_letter not in view


def update_view(mystery_phrase: str, view: str, chr_index: int,
                chr_guess: str) -> str:

    """Return the reveal of the character in view if chr_guess is
    correct else current_view stays the same.

    Preconditions: view and chr_index are valid for mystery_phrase
    and chr_guess is one character long.

    >>> update_view('line', 'l^n^', 1, 'i')
    'i'
    >>> update_view('drawing', '^ra^^ng', 0, 'c')
    '^'
    >>> update_view('bottle', 'b^t^^e', 3, 't')
    't'
    >>> update_view('water', '^^te^', 4, 's')
    '^'
    """
    if mystery_phrase[chr_index] == chr_guess:
        return chr_guess
    return view[chr_index]


def compute_score(current_score: int, num_occ: int, current_move: str) -> int:

    """Return the sum of current_score and POINTS_PER_GUESS if currrent_move
    is 'Guess a consonant' and consonant is guessed correctly, else the
    current_score stays the same.

    Preconditions: current_move is either 'Guess consonant'(G) or 'Buy a vowel'
    (B) and current_score and num_occ are non-negtive.

    >>> compute_score(4, 5, 'G')
    9
    >>> compute_score(9, 12, 'G')
    21
    >>> compute_score(10, 9, 'B')
    9
    """
    if current_move == 'G':
        return current_score + (num_occ * POINTS_PER_GUESS)
    return current_score - COST_OF_VOWEL


def next_turn(current_player: str, num_occ: int, game_type: str) -> str:

    """Return current_player if game_type is SINGLE_PLAYER or if current_player
    guessed correctly else return the other player.

    Preconditions: current_player is a valid player, num_occ is non-negative
    and game_type is a valid game type.

    current_player is PLAYER_ONE or PLAYER_TWO.
    game_type is SINGLE_PLAYER, PVP, or PVE.

    >>> next_turn(PLAYER_ONE, 4, SINGLE_PLAYER)
    'Player One'
    >>> next_turn(PLAYER_TWO, 5, PVP)
    'Player Two'
    >>> next_turn(PLAYER_TWO, 0, PVP)
    'Player One'
    >>> next_turn(PLAYER_ONE, 3, PVP)
    'Player One'
    """
    if num_occ > 0:
        return current_player
    if game_type == PVP or PVE:
        if num_occ == 0:
            return PLAYER_TWO if current_player == PLAYER_ONE else PLAYER_ONE
    return current_player


def is_mystery_char(chr_index: int, mystery_phrase: str, view: str) -> bool:

    """Return True if and only if the character at the given index chr_index is
    currently displayed as a mystery charcater in the game.

    Precondition: chr_index is a valid non-negative index for mystery_phrase.

    >>> is_mystery_char(4, 'calculator', 'ca^^^^a^or')
    True
    >>> is_mystery_char(2, 'reading week', 'rea^^ng w^^k')
    False
    >>> is_mystery_char(5, 'holidays', 'h^^^^^^s')
    True
    >>> is_mystery_char(2, 'nothing at all', 'n^t^^ng a^ ^^^')
    False
    """
    return not mystery_phrase[chr_index] in view


def environment_solves(view: str, difficulty: str,
                       csnt_not_guessed: str) -> bool:

    """Return True iff the computer decides to solve the mystery
    phrase in a PVE game. If game difficulty is HARD, the computer chooses to
    solve if at least half of the letters have been revealed or if there are no
    more csnt_not_guessed. If game difficulty is EASY,
    the computer chooses to solve if there are no more consonants
    to choose from. Else, the computer does not choose to solve.

    Precondition: game_type is PVE.

    game_difficulty can be EASY or HARD.

    >>> environment_solves('co^^^^^^', HARD, 'm, p, t, r')
    False
    >>> environment_solves('ma^^y', HARD, 'r')
    True
    >>> environment_solves('g^^e', EASY, 'm')
    False
    """
    return difficulty == HARD and (half_solved(view) or csnt_not_guessed == '')


def delete(letters_string: str, chr_index: int) -> str:

    """Return the given letters in letters_string with the character at
    chr_index removed if 0 < chr_index < index of last character in the string
    else return the original string of letters unchanged.

    >>> delete('apple', 2)
    'aple'
    >>> delete('canada', 1)
    'cnada'
    >>> delete('laptop', 0)
    'laptop'
    >>> delete('documents', 0)
    'documents'
    """
    if 0 < chr_index < len(letters_string) - 1:
        return letters_string[0:chr_index] + letters_string[chr_index+1:]
    return letters_string


if __name__ == '__main__':
    import doctest
    doctest.testmod()
