from ._if_not_valid_raise import _if_not_int_or_float_raise

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

def epe_calc(k, e):
    """Calculates Elastic Potential Energy using the formula:
        E = 0.5(spring constant(extension squared))

    Parameters
    ----------
    k: int or float
        The spring constant in the equation

    e: int or float
        The extension in the equation

    Returns
    -------
    Float
        0.5 * (k * (e**2))

    Raises
    ------
    ValueError
        If k or e is not an integer or a float

    Examples
    --------
    >>> school_algorithms.epe_calc(5, 10)
    250
    """

    _if_not_int_or_float_raise(k, e)
    return 0.5 * (k * (e**2))
