"""Sample solutions for the unittest worksheet."""

import unittest
from underperformers import keep_underperformers


# Note: this test suite does not contain a complete set of test cases.
class TestKeeptUnderperformers(unittest.TestCase):
    """Test the function keep_underperformers."""

    def test_keep_underperformers_low_threshold(self):
        """Test keep_underperformers with a threshold for which there are
        no underperformers.

        """

        arg_lst = [4, 5, 6]
        expected = []
        keep_underperformers(arg_lst, 1)
        msg = message("keep_underperformers([4, 5, 6], 1)",
                      str(expected), str(arg_lst))

        self.assertEqual(arg_lst, expected, msg)

    def test_keep_underperformers_high_threshold(self):
        """Test keep_underperformers with a threshold for which all items
        are underperformers.

        """

        arg_lst = [4, 5, 6]
        expected = [4, 5, 6]
        keep_underperformers(arg_lst, 10)
        msg = message("collect_underperformers([4, 5, 6], 10)",
                      str(expected), str(arg_lst))
        self.assertEqual(arg_lst, expected, msg)

    # many more tests are needed!

    def test_returns_none(self):
        """Test that keep_underperformers returns None.

        """

        result = keep_underperformers([1, 2, 3], 10)
        self.assertEqual(result, None,
                         "keep_underperformers should return None")


def message(test_case: str, expected: str, actual: str) -> str:
    """Return an error message for the function call test_case that
    is expected to modify its argument to expected, but the argument
    after the call is actual.
    """

    return ("When we called " + test_case
            + " we expected the argument to be " + expected
            + ", but it was " + actual)


if __name__ == '__main__':
    unittest.main(exit=False)
