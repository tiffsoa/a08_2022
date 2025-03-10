"""Code for worksheet on nested lists and nested loops."""


def digital_sum(nums_list: list[str]) -> int:
    """Return the sum of all the digits in all strings in nums_list.
    If nums_list is empty, return 0.

    Precondition: s.isdigit() holds for each string s in nums_list.

    >>> digital_sum(['64', '128', '256'])
    34
    >>> digital_sum(['12', '3'])
    6
    >>> digital_sum([])
    0
    >>> digital_sum(['0'])
    0
    >>> digital_sum(['9'])
    9

    """

    total = 0
    for num in nums_list:
        for digit in num:
            total = total + int(digit)

    return total


def can_pay_with_two_coins(denoms: list[int], amount: int) -> bool:
    """Return True if and only if it is possible to form amount, a number
    of cents, using two coins of any of the denominations in denoms.

    Pre: each element of denoms is positive
         amount >= 0

    >>> can_pay_with_two_coins([1, 5, 10, 25], 35)
    True
    >>> can_pay_with_two_coins([1, 5, 10, 25], 20)
    True
    >>> can_pay_with_two_coins([1, 5, 10, 25], 12)
    False
    >>> can_pay_with_two_coins([1, 5, 10, 25], 1)
    False
    >>> can_pay_with_two_coins([25], 25)
    False
    >>> can_pay_with_two_coins([25], 50)
    True
    >>> can_pay_with_two_coins([25], 55)
    False
    >>> can_pay_with_two_coins([], 0)
    False
    >>> can_pay_with_two_coins([], 42)
    False

    """

    for coin1 in denoms:
        for coin2 in denoms:
            if coin1 + coin2 == amount:
                return True
    return False

    # solution with one loop (not all languages support an operation
    # like "in" though, so make sure you understand the first
    # solution!)
    # for coin in denoms:
    #     if amount - coin in denoms:
    #         return True
    # return False
    # is this solution faster? No! The operation "in" is not free!

    # can we come up with a solution that is actually faster? Yes!
    # for i in range(len(denoms)):
    #     for j in range(i, len(denoms)):
    #         if denoms[i] + denoms[j] == amount:
    #             return True
    # return False


if __name__ == '__main__':

    import doctest
    doctest.testmod()
