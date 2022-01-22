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

def circumference2(d):
    """Calculates the circumference of a cirle using the formula:
        \u03C0 * diameter

    Parameters
    ----------
    d: int or float
        The diameter in the equation.

    Returns
    -------
        Float
            \u03C0 * d

    Raises
    ------
    ValueError
        If d::
            Is not an integer or float.
            Is not positive.

    Examples
    --------
    >>> school_algorithms.circumference2(10)
    31.415926535898

    """
    _if_not_int_or_float_raise(d)
    _if_not_positive_raise(d)
    return _pi * d

def area_of_sector(r, a):
    """A function that calculates the area of a sector in a circle:
      angle/360 * \u03C0 * (r squared)

    Parameters
    ----------
    r: int or float
      The radius in the equation.

    a: int or float
      The angle in the equation.

    Returns
    -------
      Float
          a/360 * \u03C0 * r**2

    Raises
    ------
    ValueError
      If a or r::
          Is not an integer or float.
          Is not positive.

    Examples
    --------
    >>> school_algorithms.area_of_sector(5, 40)
    8.726646259971647

    """
    _if_not_int_or_float_raise(r, a)
    _if_not_positive_raise(r, a)
    return a/360 * _pi * r**2
