from math import sqrt as _sqrt
from ._if_not_valid_raise import (_if_not_int_or_float_raise,
                                         _if_negative_raise)
def pythag_leg(hy, a):
    """
    Calculates the length of a leg in right-angled triangle using the formula:
        leg(b) = the square-root of (hy squared - leg(a) squared)

    Parameters
    ----------
    hy: int or float
        The hypotneus of the equation.

    a: int or float
        The leg of the equation.

    Returns
    -------
    Float
        sqrt(a**2 + b**2)

    Raises
    ------
    ValueError
        If hy or a is not an integer or float.
        If hy or a is a negative number

    Examples
    --------
    >>> school_algorithms.pythag_leg(7, 2)
    6.708203932499369

    """
    _if_not_int_or_float_raise(hy, a)
    _if_negative_raise(hy, a)
    return _sqrt(hy**2 - a**2)

def pythag_hypot(a, b):
    """
    Calculates the hypotenuse of a right angled triangle using the formula:
        hypotenuse = the square-root of (leg(a) squared + leg(b) squared)

    Parameters
    ----------
    a: int or float
        leg(a) of the equation.
    b: int or float
        leg(b) of the equation.

    Returns
    -------
    Float
        sqrt(a**2 + b**2)

    Raises
    ------
    ValueError
        If a or b is not an integer or float
        If a or b is a negative number

    Examples
    --------
    >>> school_algorithms.pythag_hypot(4, 2)
    4.47213595499958

    """
    _if_not_int_or_float_raise(a, b)
    _if_negative_raise(a, b)
    return _sqrt(a**2 + b**2)
