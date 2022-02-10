"""
school_algorithms
=================

school_algorithms is a Python module for secondary school
maths and physics equations.

It aims to provide a simple way for secondary school students
to learn and calculate equations that they often use.

How to use documentation
------------------------
Documentation is provided in the form of docstrings provided
with the code.

The docstring examples assume that 'school_algorithms' has been imported::

    >>> import school_algorithms

Code snippets are indicated by three greater-than signs

    >>> x = 42
    >>> x = x + 1

Use the built-in ``help`` function to view a function's docstring::

    >>> help(school_algorithms.power_calc)

Functions
---------
power_calc
    A function that calculates power from energy and time

energy_calc
    A function that calculates energy from power and time

time_calc
    A function that calculates time from power and energy

pythag_hypot
    A function that uses Pythagorean theorem to calculate the hypotenuse
    of a right-angled triangle

pythag_leg
    A function that uses Pythagorean theorem to calculate a leg
    of a right-angled triangle

triangle_area
    A function that calculates the area of a triangle

trapezium_area
    A function that calculates the area of a trapezium

circle_area
    A function that calculates the area of a circle

right_rect_pyramid
    A function that calculates the volume of a right rectangle pyramid

epe_calc
    A function that calculates Elastic Potential Energy

kinetic_calc
    A function that calculates Kinetic Energy

circumference
    A function that calculates the circumference of a circle

circumference2
    A function that calculates the circumference of a circle
    using the diameter

circumference2
    A function that calculates the circumference of a circle
    using the diameter

square_pyramid
    A function that calculates the volume of a square based pyramid

lcm
    A function that calculates the Lowest Common Multiple (lcm) from any amount of numbers

area_of_sector
    A function that calculates the area of a sector in a circle

"""
from .circle import *
from .physics import *
from .pythagorus import *
from .trapezium import *
from .triangle import *
from .pyramid import *
from .lcm import lcm
