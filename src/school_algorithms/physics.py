from ._if_not_valid_raise import _if_not_int_or_float_raise

def power_calc_from_energy_and_time(E, t):
    """Calculates power from energy and time using the formula:
        power = energy / time

    Parameters
    ----------
    E : int or float
        The energy value in the equation.

    t : int or float
        The time value of the equation (seconds).

    Returns
    -------
    Float
         E / t

    Raises
    ------
    ValueError
        If E or t is not an integer or float.

    Examples
    --------
    >>> school_algorithms.power_calc(10, 5)
    2.0

    """
    _if_not_int_or_float_raise(E, t)
    return E / t

def power_calc_from_work_and_time(W, t):
    _if_not_int_or_float_raise(W, t)

    return W / t

def power_calc_from_potential_diff_and_current(V, I):
    _if_not_int_or_float_raise(V, I)

    return V * I 

def power_calc_from_current_and_resistance(I, R):
    _if_not_int_or_float_raise(I, R)

    return I**2 * R

def energy_calc(p, t):
    """
    Calculates energy from power and time using the formula:
        energy = power * time

    Parameters
    ----------
    p: Int or float
        The power value of the equation.

    t: Int or float
        The time value of the equation (seconds).

    Returns
    -------
    Int
        p * t

    Raises
    ------
    ValueError
        If p or t is not an integer or float.

    Examples
    --------
    >>> school_algorithms.energy_calc(5, 2)
    10

    """
    _if_not_int_or_float_raise(p, t)
    return p * t

def time_calc_from_power_and_energy(p, E):
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
        If p or E is not an integer or float.

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
        The spring constant in the equation.

    e: int or float
        The extension in the equation.

    Returns
    -------
    Float
        0.5 * (k * (e**2))

    Raises
    ------
    ValueError
        If k or e is not an integer or a float.

    Examples
    --------
    >>> school_algorithms.epe_calc(5, 10)
    250
    """
    _if_not_int_or_float_raise(k, e)
    return 0.5 * (k * (e**2))

def kinetic_calc(s ,m):
    """Calculates Elastic Potential Energy using the formula:
        kinetic energy = 0.5 × mass × (speed)^2

    Parameters
    ----------
    s: int or float
        The speed value in the equation.

    m: int or float
        The mass value in the equation.

    Returns
    -------
    Float
        0.5 * m * s**2

    Raises
    ------
    ValueError
        If m or s is not an integer or a float.

    Examples
    --------
    >>> school_algorithms.kinetic_calc(5, 10)
    125
    """
    _if_not_int_or_float_raise(m, s)
    return 0.5 * m * s**2

def change_in_thermal_energy_calc(m, c, delta_T):
    _if_not_int_or_float_raise(m, c, delta_T)

    return m * c * delta_T

def grav_pot_energy_calc(m, g, h):
    _if_not_int_or_float_raise(m, s)

    return m * g * h 

def efficiency_calc_from_power(output_p, input_p):
    _if_not_int_or_float_raise(output_p, input_p)

    return output_p / input_p

def efficiency_calc_from_energy(output_E, input_E):
    _if_not_int_or_float_raise(output_E, input_E)

    return output_E / input_E

def charge_flow_calc(I, t):
    _if_not_int_or_float_raise(m, s)

    return I * t

def potential_diff_calc(I, R):
    _if_not_int_or_float_raise(I, R)

    return I * R

def energy_transfered_calc_from_power_and_time(p, t):
    _if_not_int_or_float_raise(p, t)

    return p * t

def energy_transfered_calc_from_charge_flow_and_potential_diff(Q, V):
    _if_not_int_or_float_raise(Q, V)

    return Q * V

def density_calc(m, V):
    _if_not_int_or_float_raise(m, V)

    return m / V

def work_done_calc(F, s):
    _if_not_int_or_float_raise(F, d)

    return F * d

def spring_force_calc(k, e):
    _if_not_int_or_float_raise(k, e)

    return k * e

def moment_of_force_calc(F, d):
    _if_not_int_or_float_raise(F, d)

    return F * d

def pressure_calc(F, A):
    _if_not_int_or_float_raise(F, A)

    return F / A

def distance_travelled_calc(v, t):
    _if_not_int_or_float_raise(v, t)

    return v * t

def acceleration_calc(delta_v, t):
    _if_not_int_or_float_raise(delta_v, t)

    return delta_v / t

def resultant_force_calc(m, a):
    _if_not_int_or_float_raise(m, a)

    return m * a

def momentum_calc(m, v):
    _if_not_int_or_float_raise(m, v)

    return m * v

def force_calc_from_change_in_momentum_and_time(delta_m, t):
    _if_not_int_or_float_raise(delta_m, t)

    return delta_m / t

def wave_speed_calc(f, wl):
    _if_not_int_or_float_raise(f, wl)

    return f * wl

def magnification_calc(image_h, object_h):
    _if_not_int_or_float_raise(image_h, object_h)

    return image_h / object_h