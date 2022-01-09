"""School algorithm module for Python
==================================

school_algorithms is a Python module for secondary school
maths and physics eqautions.

It aims to provide a simple way for secondary school students
to learn and calculate equations that the often use.
"""

from math import sqrt as _sqrt, pi as _pi


def _if_not_int_or_float_raise(*args):
    for arg in args:
        if type(arg) != int and type(arg) != float:
            raise ValueError ("At least, one of the values wasn't an integer or a float.")

def power_calc(E, t):
    """Calculates power from energy and time using the formula:
        power = energy / time

    Parameters
    ----------
    E : int or float
        The energy value in the equation.

    t : int or float
        The time value of the equation.

    Returns
    -------
    Float
         E / t

    Raises
    ------
    ValueError
        If E or t is not an integer or float

    Examples
    --------
    >>> school_algorithms.power_calc(10, 5)
    2.0

    """
    _if_not_int_or_float_raise(E, t)
    return E / t

def energy_calc(p, t):
    """
    Calculates energy from power and time using the formula:
        energy = power * time

    Parameters
    ----------
    p: Int or float
        The power value of the equation.

    t: Int or float
        The time value of the equation.

    Returns
    -------
    Int
        p * t

    Raises
    ------
    ValueError
        If p or t is not an integer or float

    Examples
    --------
    >>> school_algorithms.energy_calc(5, 2)
    10

    """
    _if_not_int_or_float_raise(p, t)
    return p * t

def time_calc(p, E):
    """
    Calculates time from power and energy using the formula:
        time = energy / power

    Parameters
    ----------
    p: int or float
        The power value of the equation.

    E: int or float
        The energy value of the equaton.

    Returns
    -------
    Float
        E / p

    Raises
    ------
    ValueError
        If p or E is not an integer or float

    Examples
    --------
    >>> school_algorithms.energy_calc(10, 2)
    5.0

    """
    _if_not_int_or_float_raise(p, E)
    return E / p

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

    Examples
    --------
    >>> school_algorithms.pythag_hypot(4, 2)
    4.47213595499958

    """
    _if_not_int_or_float_raise(a, b)
    return _sqrt(a**2 + b**2)

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

    Examples
    --------
    >>> school_algorithms.pythag_leg(7, 2)
    6.708203932499369

    """
    _if_not_int_or_float_raise(hy, a)
    return _sqrt(hy**2 - a**2)

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
         If c b or h is not an integer or float

    Examples
    --------
    >>> school_algorithms.trapezium_area(4, 5, 6)
    27.0

    """
    _if_not_int_or_float_raise(c, b, h)
    return ((c + b) / 2) * h

def circle_area(r):
    """
    Calculates the area of a trapezium using the formula:
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
        If r is not an integer or float

    Examples
    --------
    >>> school_algorithms.circle_area(10)
    314.1592653589793

    """
    _if_not_int_or_float_raise(r)
    return _pi * (r**2)
