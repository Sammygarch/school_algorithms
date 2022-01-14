from math import pi as _pi
from ._if_not_valid_raise import (_if_not_int_or_float_raise,
                                   _if_not_positive_raise)


def circle_area(r):
    """Calculates the area of a trapezium using the formula:
        area = \u03C0(radius squared)

    Parameters
    ----------
    r: int or float
        The radius in the equation.

    Returns
    -------
        Float
            \u03C0 * (r**2)

    Raises
    ------
    ValueError
        If r::
            Is not an integer or float.
            Is not positive.

    Examples
    --------
    >>> school_algorithms.circle_area(10)
    314.1592653589793

    """
    _if_not_int_or_float_raise(r)
    _if_not_positive_raise(r)
    return _pi * (r**2)

def circumference(r):
    """Calculates the circumference of a cirle using the formula:
        2\u03C0radius

    Parameters
    ----------
    r: int or float
        The radius in the equation.

    Returns
    -------
        Float
            \u03C0 * r * 2

    Raises
    ------
    ValueError
        If r::
            Is not an integer or float.
            Is not positive.

    Examples
    --------
    >>> school_algorithms.circumference(5)
    31.415926535898

    """
    _if_not_int_or_float_raise(r)
    _if_not_positive_raise(r)
    return _pi * r * 2
