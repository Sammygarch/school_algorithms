"""School algorithm module for Python
==================================

school_algorithms is a Python module for secondary school
maths and physics eqautions.

It aims to provide a simple way for secondary school students
to learn and calculate equations that the often use.
"""

from math import sqrt as _sqrt
from math import pi as _pi

def _if_not_int_or_float_raise(*args):
    for arg in args:
        if type(arg) != int and type(arg) != float:
            raise ValueError ("At least, one of the values wasn't an integer or a float.")

def power_calc(E, t):
    """
    Calculates power from energy and time using the formula:
        power = energy / time

    Args:
        E (int or float): The energy value in the equation
        t (int or float): The time value of the equation

    Returns:
        Float: E / t

    Raises:
        ValueError: If E or t is not an integer or float

    """
    _if_not_int_or_float_raise(E, t)
    return E / t

def energy_calc(p, t):
    """
    Calculates energy from power and time using the formula:
        energy = power * time

    Args:
        p (int or float): The power value of the equation
        t (int or float): The time value of the equation

    Returns:
        p * t

    Raises:
        ValueError: If p or t is not an integer or float

    """
    _if_not_int_or_float_raise(p, t)
    return p * t

def time_calc(p, E):
    """
    Calculates time from power and energy using the formula:
        time = energy / power

    Args:
        p (int or float): The power value of the equation
        E (int or float): The energy value of the equaton

    Returns:
        Float: E / p

    Raises:
        ValueError: If p or E is not an integer or float

    """
    _if_not_int_or_float_raise(p, E)
    return E / p

def pythag_hypot(a, b):
    """
    Calculates the hypotenuse of a right angled triangle using the formula:
        hypotenuse = the square-root of (leg(a) squared + leg(b) squared)

    Args:
        a (int or float): leg(a) of the equation
        b (int or float): leg(b) of the equation

    Returns:
        Float: sqrt(a**2 + b**2)

    Raises:
        ValueError: If a or b is not an integer or float

    """
    _if_not_int_or_float_raise(a, b)
    return _sqrt(a**2 + b**2)

def pythag_leg(hy, a):
    """
    Calculates the length of a leg in right-angled triangle using the formula:
        leg(b) = the square-root of (hy squared - leg(a) squared)

    Args:
        hy: the hypotneus of the equation
        a: the leg of the equation

    Returns:
        Float: sqrt(a**2 + b**2)

    Raises:
        ValueError: If hy or a is not an integer or float

    """
    _if_not_int_or_float_raise(hy, a)
    return _sqrt(hy**2 - a**2)

def triangle_area(b, h):
    """
    Calculates the  area of a triangle using the formula:
        area = (base * height)/2

    Args:
        b(int or float): the base in the equation
        h(int or float): the height in the equation

    Returns:
        Float: (b*h) / 2

    Raises:
        ValueError: If b or h is not an integer or float
    """
    _if_not_int_or_float_raise(b, h)
    return (b*h) / 2

def trapezium_area(c, b, h):
    """
    Calculates the area of a trapezium using the formula:
        area = ((ceiling + base) / 2) * height

    Args:
        c(int or float): the ceiling in the equation
        b(int or float): the base in the equation
        h(int or float): the height in the equation

    Returns:
        Float: ((c + b) / 2) * h

    Raises:
        ValueError: If c b or h is not an integer or float

    """
    _if_not_int_or_float_raise(c, b, h)
    return ((c + b) / 2) * h

def circle_area(r):
    """
    Calculates the area of a trapezium using the formula:
        area = \u03C0(radius squared)

    Args:
        r(int or float): the radius in the equation

    Returns:
        Float: \u03C0 * (r**2)

    Raises:
        ValueError: If r is not an integer or float
    """
    _if_not_int_or_float_raise(r)
    return _pi * (r**2)
