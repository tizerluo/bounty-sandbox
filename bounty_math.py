"""Integer arithmetic helpers for the IssueBountyEscrow live demo (issue #1)."""


def add(a: int, b: int) -> int:
    """Return the sum of two integers.

    >>> add(2, 3)
    5
    >>> add(-4, 1)
    -3
    """
    if type(a) is not int or type(b) is not int:
        raise TypeError("add() expects two integers")
    return a + b
