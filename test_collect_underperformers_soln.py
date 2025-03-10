"""Sample solutions for the unittest worksheet."""

import unittest
from underperformers import collect_underperformers


# Note: this test suite does not contain a complete set of test cases.
class TestCollectUnderperformers(unittest.TestCase):
    """Test the function collect_underperformers."""

    def test_underperformers_low_threshold(self):
        """Test collect_underperformers with a threshold for which there are
        no underperformers.

        """

        actual = collect_underperformers([4, 5, 6], 1)
        expected = []
        msg = message("collect_underperformers([4, 5, 6], 1)",
                      str(expected), str(actual))
        self.assertEqual(actual, expected, msg)

    def test_underperformers_high_threshold(self):
        """Test collect_underperformers with a threshold for which all items
        are underperformers.

        """

        actual = collect_underperformers([4, 5, 6], 10)
        expected = [4, 5, 6]
        msg = message("collect_underperformers([4, 5, 6], 10)",
                      str(expected), str(actual))
        self.assertEqual(actual, expected, msg)

    # many more test methods are needed here

    def test_underperformers_mutation(self):
        """Confirm that collect_underperformers does not mutate the input
        list.

        """

        arg_lst = [4, 5, 6]
        exp_lst = [4, 5, 6]
        collect_underperformers(arg_lst, 5)
        msg = ("collect_underperformers([4, 5, 6], 5) modified the input!"
               + "We expected the input to stay " + str(exp_lst)
               + ", but found it changed to " + str(arg_lst))
        self.assertEqual(arg_lst, exp_lst, msg)


def message(test_case: str, expected: str, actual: str) -> str:
    """Return an error message for the function call test_case that
    resulted in a value actual, when the correct value is expected.

    """

    return ("When we called " + test_case + " we expected " + expected
            + ", but got " + actual)


if __name__ == '__main__':
    unittest.main(exit=False)
