"""Week 3 worksheet problems: sample solution."""


def ticket_price(age: int) -> float:
    """Return the ticket price for a person who is age years old.  Seniors
    65 and over pay 4.75, kids 12 and under pay 4.25 and everyone else
    pays 7.50.

    Precondition: age >= 0

    >>> ticket_price(7)
    4.25
    >>> ticket_price(21)
    7.5
    >>> ticket_price(101)
    4.75

    """

    if age >= 65:
        return 4.75
    if age <= 12:
        return 4.25
    return 7.5


def ticket_book_price(age: int, num_tickets: int) -> float:
    """Return the price of a booklet of num_tickets tickets for a person
    who is age years old. Orders of 10 or more tickets receive a 10%
    discount. Before discount, seniors 65 and over pay 4.75, kids 12
    and under pay 4.25 and everyone else pays 7.50.

    Precondition: age >= 0
                  num_tickets >= 0

    >>> ticket_book_price(7, 5)
    21.25
    >>> ticket_book_price(21, 10)
    67.5
    >>> ticket_book_price(101, 1)
    4.75

    """

    price = ticket_price(age) * num_tickets
    if num_tickets >= 10:
        return 0.9 * price
    return price


if __name__ == '__main__':
    import doctest
    doctest.testmod()
