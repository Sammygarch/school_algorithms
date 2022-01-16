from ._if_not_valid_raise import (_if_not_int_or_float_raise,
                                  _if_not_positive_raise)

def trapezium_area(c, b, h):
    """
    Calculates the area of a trapezium using the formula:
        area = ((ceiling + base) / 2) * height

    Parameters
    ----------
    c: int or float
        The ceiling in the equation.

    b: int or float
        The base in the equation.

    h: int or float
        The height in the equation.

    Returns
    -------
    Float
        ((c + b) / 2) * h

    Raises
    ------
    ValueError
         If c b or h::
            Is not an integer or float.
            Is not positive.

    Examples
    --------
    >>> school_algorithms.trapezium_area(4, 5, 6)
    27.0

    """
    _if_not_int_or_float_raise(c, b, h)
    _if_not_positive_raise(c, b, h)
    return ((c + b) / 2) * h
