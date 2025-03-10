"""Generating a random story: sample solutions.
"""

from typing import TextIO
import random


def generate_random_story(data_file: TextIO, context_size: int,
                          num_words: int) -> str:
    """Return a randomly generated story with num_words words based on a
    context of context_size words from the text in data_file.

    Preconditions: data_file is open for reading
                   context_size > 0
                   num_words >= 0
    """

    all_words = read_words(data_file)
    context_to_words = build_context_to_words(all_words, context_size)
    return generate_story(context_to_words, num_words)


def read_words(data_file: TextIO) -> list[str]:
    """Return a list of words from data_file. Words are defined as all
    strings delimited by whitespace.
    """

    return data_file.read().split()


def build_context_to_words(word_list: list[str],
                           context_size: int) -> dict[tuple, list[str]]:
    """Return a dictionary where each key is a tuple of context_size
    adjacent words from word_list, and each corresponding value is a
    list of words that immediately follow these adjacent words in
    word_list.

    Preconditions: context_size > 0

    >>> context_to_words = build_context_to_words(
    ...    ['to', 'be', 'or', 'not', 'to', 'be', 'that'], 2)
    >>> context_to_words == {('to', 'be'): ['or', 'that'],
    ...                      ('be', 'or'):['not'],
    ...                      ('or', 'not'):['to'],
    ...                      ('not', 'to'): ['be']}
    True
    >>> context_to_words = build_context_to_words(
    ...    ['to', 'be', 'or', 'not', 'to', 'be', 'or'], 2)
    >>> context_to_words == {('to', 'be'): ['or', 'or'], # decision!
    ...                      ('be', 'or'):['not'],
    ...                      ('or', 'not'):['to'],
    ...                      ('not', 'to'): ['be']}
    True
    >>> build_context_to_words([], 2)
    {}
    >>> build_context_to_words(['foo'], 1)
    {}
    >>> build_context_to_words(['foo', 'bar'], 1)
    {('foo',): ['bar']}
    >>> build_context_to_words(['foo', 'bar'], 2)
    {}
    >>> expected = {('foo', 'bar'): ['foobar']}
    >>> build_context_to_words(['foo', 'bar', 'foobar'], 2) == expected
    True
    """

    context_to_words = {}

    for i in range(len(word_list) - context_size):
        context = tuple(word_list[i: i + context_size])  # make key
        word = word_list[i + context_size]               # make new value

        if context in context_to_words:
            context_to_words[context].append(word)
        else:
            context_to_words[context] = [word]

    return context_to_words


def generate_story(context_to_words: dict[tuple, list[str]],
                   num_words: int) -> str:
    """Return a randomly generated story with num_words words based on a
    context_to_words.

    Preconditions: num_words >= 0
    """

    story = ''  # accumulator variable

    context = get_random_context(context_to_words)

    for _ in range(num_words):
        words = context_to_words[context]     # possible next words
        next_word = random.choice(words)
        story += ' ' + next_word

        context = context[1:] + (next_word,)  # next context

        # if words in context were at the end of the file
        if context not in context_to_words:
            context = get_random_context(context_to_words)

    return story


# A helper function
def get_random_context(context_to_words: dict[tuple, list[str]]) -> tuple:
    """Return a random context (key) from context_to_words."""

    return random.choice(list(context_to_words.keys()))


if __name__ == '__main__':

    import doctest
    doctest.testmod()

    with open('small.txt') as small:
        print(generate_random_story(small, 2, 10))

    # filename = input('Enter a filename: ')
    # with open(filename) as training_file:
    #     print(generate_random_story(training_file, 2, 50))
