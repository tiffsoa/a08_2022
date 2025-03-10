"""Sample solution for the worksheet on dictionaries.
"""

EXPRESS_MAX = 8


def express_checkout(product_to_quantity: dict[str, int]) -> bool:
    """Return True if and only if the grocery order in product_to_quantity
    qualifies for the express checkout. product_to_quantity maps
    products to the numbers of those products in the grocery order.

    Precondition: all values in product_to_quantity are non-negative.

    >>> express_checkout({'banana': 3, 'soy milk': 1, 'peanut butter': 1})
    True
    >>> express_checkout({'banana': 3, 'soy milk': 1, 'twinkie': 7})
    False
    >>> express_checkout({'banana': 3, 'soy milk': 1, 'twinkie': 5})
    False
    >>> express_checkout({})
    True
    >>> express_checkout({'milk': 8})
    True
    >>> express_checkout({'milk': 9})
    False

    """

    # quantities = []
    # for product in product_to_quantity:
    #     quantities.append(product_to_quantity[product])
    # return sum(quantities) <= EXPRESS_MAX
    # problems: Need to go over the quantities twice: once to build a
    # list, and then again to sum the list. Also, need to store the
    # list!
    # much better:
    total = 0
    for product in product_to_quantity:
        total = total + product_to_quantity[product]
    return total <= EXPRESS_MAX

    # OR:
    # total = 0
    # for quantity in product_to_quantity.values():
    #     total = total + quantity
    # return total <= EXPRESS_MAX

    # OR:
    # return sum(product_to_quantity.values()) <= EXPRESS_MAX

    # OR (is this faster? difficult question! potentially yes, if
    #     we expect mostly large shopping carts)
    # total = 0
    # for quantity in product_to_quantity.values():
    #     total = total + quantity
    #     if total > EXPRESS_MAX:
    #         return False
    # return True


def build_placements(shoes_at_finish_line: list[str]) -> dict[str, list[int]]:
    """Return a dictionary built from the information in
    shoes_at_finish_line, where each key is a brand and each value is
    a list of placements by people wearing shoes made by that
    company. shoes_at_finish_line contains shoe brands in order, in
    which they appeared at the finish line.

    >>> result = build_placements(['Saucony', 'Asics', 'Asics', 'NB',
    ...                            'Saucony', 'Nike', 'Asics', 'Adidas',
    ...                            'Saucony', 'Asics'])
    >>> result == {'Saucony': [1, 5, 9], 'Asics': [2, 3, 7, 10], 'NB': [4],
    ...                        'Nike': [6], 'Adidas': [8]}
    True
    >>> build_placements([])
    {}
    >>> build_placements(['Nike']) == {'Nike': [1]}
    True
    >>> build_placements(['NB', 'NB', 'NB']) == {'NB': [1, 2, 3]}
    True
    >>> result = build_placements(['NB', 'Nike', 'NB', 'Nike', 'NB'])
    >>> result == {'NB': [1, 3, 5], 'Nike': [2, 4]}
    True

    """

    brand_to_placement = {}

    for i in range(len(shoes_at_finish_line)):
        brand = shoes_at_finish_line[i]
        if brand in brand_to_placement:
            brand_to_placement[brand].append(i + 1)
        else:
            brand_to_placement[brand] = [i + 1]

    return brand_to_placement


if __name__ == '__main__':
    import doctest
    doctest.testmod()
