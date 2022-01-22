from ._if_not_valid_raise import _if_not_int_raise
from math import gcd as _gcd

def lcm(a, b):
    """Calculates the Lowest Common Multiple from 2 numbers.

    Parameters
    ----------
    a, b: int

    Returns
    -------
    Int
        The Lowest Common Multiple (lcm) of a and b.

    Raises
    ------
    ValueError
        If a or b is not an integer

    Examples
    --------
    >>> school_algorithms.lcm(5, 7)
    35
    """
    _if_not_int_raise(a, b)
    gcd = _gcd(a, b)
    return int((a * b) / gcd)

def lcm_3_nums(a, b, c):
    """Calculates the Lowest Common Multiple from 3 numbers.

    Parameters
    ----------
    a, b, c: int

    Returns
    -------
    Int
        The Lowest Common Multiple (lcm) of a, b and c.

    Raises
    ------
    ValueError
        If a, b or c  is not an integer

    Examples
    --------
    >>> school_algorithms.lcm_3_nums(5, 9, 10)
    90
    """
    _if_not_int_raise(a, b, c)
    ab_lcm = lcm(a, b)
    return int(lcm(ab_lcm, c))

def lcm_4_nums(a, b, c, d):
    """Calculates the Lowest Common Multiple from 4 numbers.

    Parameters
    ----------
    a, b, c, d: int

    Returns
    -------
    Int
        The Lowest Common Multiple (lcm) of a, b, c and d.

    Raises
    ------
    ValueError
        If a, b, c or d  is not an integer

    Examples
    --------
    >>> school_algorithms.lcm_4_nums(5, 9, 10, 15)
    90
    """
    _if_not_int_raise(a, b, c, d)
    return int(lcm(lcm(lcm(a, b), c), d))
