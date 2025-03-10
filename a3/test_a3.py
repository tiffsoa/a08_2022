"""CSCA08: Fall 2022 -- Assignment 3: Hypertension and Low Income

Starter code for tests to test function get_bigger_neighbourhood in
a3.py.

This code is provided solely for the personal and private use of
students taking the CSC108/CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2022 Jacqueline Smith, David Liu, and Anya Tafliovich

"""

import copy
import unittest
from a3 import get_bigger_neighbourhood as gbn
from a3 import SAMPLE_DATA

SAMPLE_2 = {
    'Halifax': {
        'id': 1,
        'hypertension': [345, 4234, 532, 3452, 6254, 25895],
        'total': 35156, 'low_income': 7638},
    'Bedford': {
        'id': 2,
        'hypertension': [23, 453, 1234, 6735, 34, 566],
        'total': 8000, 'low_income': 5000},
    'Sackville': {
        'id': 3,
        'hypertension': [34, 65, 345, 533, 4352, 5543],
        'total': 6200, 'low_income': 4932}
}

SAMPLE_3 = {
    'Mile-End': {
        'id': 1,
        'hypertension': [2345, 6357, 3445, 4668, 45, 78],
        'total': 11300, 'low_income': 8000},
    'Montreal': {
        'id': 2,
        'hypertension': [3749, 6739, 465, 678, 8374, 10093],
        'total': 18000, 'low_income': 15739},
    'Plato': {
        'id': 3,
        'hypertension': [44, 245, 8473, 9384, 3845, 4975],
        'total': 15500, 'low_income': 12938},
    'Centre': {
        'id': 4,
        'hypertension': [374, 3749, 4654, 5946, 4834, 5738],
        'total': 15500, 'low_income': 13948}
    }


class TestGetBiggerNeighbourhood(unittest.TestCase):
    """Test the function get_bigger_neighbourhood."""

    def test_first_bigger(self):
        """Test that get_bigger_neighbourhood correctly returns the first
        neighbourhood when its population is strictly greater than the
        population of the second neighbourhood and both are keys in the CityData
        dictionary.

        """

        sample_data_copy = copy.deepcopy(SAMPLE_DATA)
        expected = 'Rexdale-Kipling'
        actual = gbn(SAMPLE_DATA, 'Rexdale-Kipling', 'Elms-Old Rexdale')
        msg = message(sample_data_copy, expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_second_bigger(self):
        """Test that get_bigger_neighbourhood correctly returns the second
        neighbourhood when its population is strictly greater than the
        population of the first neighbourhood and both are keys in the CityData
        dictionary.

        """

        sample_data_copy = copy.deepcopy(SAMPLE_DATA)
        expected = 'Montreal'
        actual = gbn(SAMPLE_3, 'Plato', 'Montreal')
        msg = message(sample_data_copy, expected, actual)
        self.assertEqual(actual, expected, msg)        

    def test_third_bigger(self):
        """Test that get_bigger_neighbourhood correctly returns the first
        neighbourhood when it is a key in the CityData dictionary and the
        second one is not.

        """

        sample_data_copy = copy.deepcopy(SAMPLE_DATA)
        expected = 'Mile-End'
        actual = gbn(SAMPLE_3, 'Mile-End', 'Halifax')
        msg = message(sample_data_copy, expected, actual)
        self.assertEqual(actual, expected, msg)        

    def test_fourth_bigger(self):
        """Test that get_bigger_neighbourhood correctly returns the second
        neighbourhood when it is a key in the CityData dictionary and the
        first one is not.

        """

        sample_data_copy = copy.deepcopy(SAMPLE_DATA)
        expected = 'Bedford'
        actual = gbn(SAMPLE_2, 'Mount Olive-Silverstone-Jamestown', 'Bedford')
        msg = message(sample_data_copy, expected, actual)
        self.assertEqual(actual, expected, msg)        

    def test_fifth_bigger(self):
        """Test that get_bigger_neighbourhood correctly returns the first
        neighbourhood when both neighbourhoods are keys in dict but they have
        the same amount of population.

        """

        sample_data_copy = copy.deepcopy(SAMPLE_DATA)
        expected = 'Plato'
        actual = gbn(SAMPLE_3, 'Plato', 'Centre')
        msg = message(sample_data_copy, expected, actual)
        self.assertEqual(actual, expected, msg)        

    def test_sixth_bigger(self):
        """Test that get_bigger_neighbourhood correctly returns the first
        neighbourhood when both neighburhoods are not keys in the dictionary.

        """

        sample_data_copy = copy.deepcopy(SAMPLE_DATA)
        expected = 'Halifax'
        actual = gbn(SAMPLE_DATA, 'Halifax', 'Montreal')
        msg = message(sample_data_copy, expected, actual)
        self.assertEqual(actual, expected, msg) 
    # TODO: add a complete test suite here


def message(test_case: dict, expected: list, actual: object) -> str:
    """Return an error message saying the function call
    get_most_published_authors(test_case) resulted in the value
    actual, when the correct value is expected.

    """

    return ("When we called get_most_published_authors(" + str(test_case) +
            ") we expected " + str(expected) +
            ", but got " + str(actual))


if __name__ == '__main__':
    unittest.main(exit=False)
