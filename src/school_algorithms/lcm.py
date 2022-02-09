from ._if_not_valid_raise import _if_not_int_raise
from math import gcd as _gcd

def _lcm(a, b):
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
    >>> school_algorithms._lcm(5, 7)
    35
    """
    _if_not_int_raise(a, b)
    gcd = _gcd(a, b)
    return int((a * b) / gcd)

def lcm(*args):
    """Calculates the Lowest Common Multiple from any amount numbers.

    Parameters
    ----------
    *args : int

    Returns
    -------
    Int
        The Lowest Common Multiple (lcm) of *args.

    Raises
    ------
    ValueError
        If any number in *args is not an integer

    Examples
    --------
    >>> school_algorithms.lcm(5)
    5
    >>> school_algorithms.lcm(5, 9)
    45
    >>> school_algorithms.lcm(5, 9, 10)
    90
    """
    _if_not_int_raise(*args)
    if len(args) == 1:
        return args[0]
    first_2 = args[:2]
    lcm = _lcm(*first_2)
    for i in args:
        if i in first_2:
            continue
        
        lcm = _lcm(lcm, i)

    return lcm

