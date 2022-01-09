from ._if_not_int_or_float_raise import _if_not_int_or_float_raise

def triangle_area(b, h):
    """
    Calculates the  area of a triangle using the formula:
        area = (base * height)/2

    Parameters
    ----------
    b: int or float
        The base in the equation.

    h: int or float
        The height in the equation.

    Returns
    -------
    Float
        (b*h) / 2

    Raises
    ------
    ValueError
        If b or h is not an integer or float.

    Examples
    --------
    >>> school_algorithms.triangle_area(4, 2)
    4.0

    """
    _if_not_int_or_float_raise(b, h)
    return (b*h) / 2
