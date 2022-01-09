import unittest

from src.school_algorithms._if_not_valid_raise import (_if_not_int_or_float_raise,
                                                              _if_not_positive_raise)
from src.school_algorithms import (circle_area,
                                   power_calc,
                                   energy_calc,
                                   time_calc,
                                   pythag_leg,
                                   pythag_hypot,
                                   trapezium_area,
                                   triangle_area)


class TestPrivFunc(unittest.TestCase):
    def test_if_not_int_or_float_raise(self):
        with self.assertRaises(ValueError):
            _if_not_int_or_float_raise("hello")
            _if_not_int_or_float_raise("1")
            _if_not_int_or_float_raise(True)
            _if_not_int_or_float_raise(5, True)
            _if_not_int_or_float_raise(True, 5)
            _if_not_int_or_float_raise(1, 5, 5, 2, 3, 4, 5, 6, 4, "hello")
            _if_not_int_or_float_raise(True, "hello")
            _if_not_int_or_float_raise("hello", 5)
            _if_not_int_or_float_raise(["hello", 3, True], 5   )
            _if_not_int_or_float_raise(["hello", 3, True])
            _if_not_int_or_float_raise({"sammy" : 1, "test": True})
            _if_not_int_or_float_raise(("hello", True, 3))
            _if_not_int_or_float_raise(("hello", True, 3))

    def test_if_not_int_or_float_raise_with_int(self):
        try:
            _if_not_int_or_float_raise(5)
            _if_not_int_or_float_raise(-4)
            _if_not_int_or_float_raise(5, 6)
            _if_not_int_or_float_raise(5, 6, -4)
            _if_not_int_or_float_raise(5, 5, 4, 3)

        except ValueError:
            assert False, f"'_if_not_int_or_float_raise' raised an exception with an int"

    def test_if_not_int_or_float_raise_with_float(self):
        try:
            _if_not_int_or_float_raise(5.0)
            _if_not_int_or_float_raise(4.5)
            _if_not_int_or_float_raise(-5.0)
            _if_not_int_or_float_raise(5.7, -6.0)
            _if_not_int_or_float_raise(5.0, 6.3, -5.9)
            _if_not_int_or_float_raise(-5.0, -6.3, -5.9, 7.3)
            _if_not_int_or_float_raise(5.0, 3.5, 7.1)

        except ValueError:
            assert False, f"'_if_not_int_or_float_raise' raised an exception with a float"

    def test_if_not_int_or_float_raise_with_float_and_int(self):
        try:
            _if_not_int_or_float_raise(4, 5.0)
            _if_not_int_or_float_raise(-0.00)
            _if_not_int_or_float_raise(4, 7.3, 5.0)
            _if_not_int_or_float_raise(4.5, 5.0, -6)
            _if_not_int_or_float_raise(4.0, 5)
            _if_not_int_or_float_raise(5.0, 6, -5.9)

        except ValueError:
            assert False, f"'_if_not_int_or_float_raise' raised an exception with a float"


    def test_if_not_positive_raise(self):
        with self.assertRaises(ValueError):
            _if_not_positive_raise(-4)
            _if_not_positive_raise(-4.0)
            _if_not_positive_raise(-4.0, 2)
            _if_not_positive_raise(-4, 5.0, 6)
            _if_not_positive_raise(0.0, -0.0)
            _if_not_positive_raise(-0.5)

    def test_if_not_positive_raise_for_no_raise(self):
        try:
            _if_not_positive_raise(4)
            _if_not_positive_raise(4.0)
            _if_not_positive_raise(4.0, 2)
            _if_not_positive_raise(6.7, 3.5, 5)

        except ValueError:
            assert False, f"'_if_not_positive_raise' raised an exception with a positive number"


class TestPhysicsAlgos(unittest.TestCase):
    def test_power_calc(self):
        self.assertEqual(power_calc(4, 2), 2.0)
        self.assertEqual(power_calc(-4, 2), -2.0)
        self.assertEqual(power_calc(4.0, 2), 2.0)
        self.assertEqual(power_calc(4.0, 2.0), 2.0)
        self.assertEqual(power_calc(-4.0, 2.0), -2.0)
        self.assertEqual(power_calc(-4.0, -2.0), 2.0)
        self.assertEqual(power_calc(4, -2), -2.0)

    def test_energy_calc(self):
        self.assertEqual(energy_calc(4, 2), 8)
        self.assertEqual(energy_calc(-4, 2), -8)
        self.assertEqual(energy_calc(4.0, 2), 8)
        self.assertEqual(energy_calc(4.0, 2.0), 8)
        self.assertEqual(energy_calc(-4.0, 2.0), -8)
        self.assertEqual(energy_calc(-4.0, -2.0), 8)
        self.assertEqual(energy_calc(4, -2), -8)


    def test_time_calc(self):
        self.assertEqual(time_calc(2, 4), 2.0)
        self.assertEqual(time_calc(2, -4), -2.0)
        self.assertEqual(time_calc(2, 4.0), 2.0)
        self.assertEqual(time_calc(2.0, 4.0), 2.0)
        self.assertEqual(time_calc(2.0, -4), -2.0)
        self.assertEqual(time_calc(-2.0, -4.0), 2.0)
        self.assertEqual(time_calc(2, -4), -2.0)

class TestMathsAlgos(unittest.TestCase):
    def test_pythag_hypot(self):
        self.assertEqual(pythag_hypot(4, 2), 4.47213595499958)
        self.assertEqual(pythag_hypot(4.0, 2), 4.47213595499958)
        self.assertEqual(pythag_hypot(4.0, 2.0), 4.47213595499958)

    def test_pythag_leg(self):
        self.assertEqual(pythag_leg(7, 2), 6.708203932499369)
        self.assertEqual(pythag_leg(7.0, 2), 6.708203932499369)
        self.assertEqual(pythag_leg(7.0, 2.0), 6.708203932499369)

    def test_triangle_area(self):
        self.assertEqual(triangle_area(4, 2), 4.0)
        self.assertEqual(triangle_area(4.0, 2), 4.0)
        self.assertEqual(triangle_area(4.0, 2.0), 4.0)

    def test_trapezium_area(self):
        self.assertEqual(trapezium_area(4, 5, 6), 27.0)
        self.assertEqual(trapezium_area(4.0, 5, 6), 27.0)
        self.assertEqual(trapezium_area(4.0, 5.0, 6), 27.0)
        self.assertEqual(trapezium_area(4.0, 5.0, 6.0), 27.0)


    def test_cirle_area(self):
        self.assertEqual(circle_area(10), 314.1592653589793)
        self.assertEqual(circle_area(10.0), 314.1592653589793)

class TestForRaisedErrors(unittest.TestCase):
    def test_physics_raised_errors(self):
        with self.assertRaises(ValueError):
            power_calc("t", "e")
            power_calc(False, True)
            power_calc(False, "t")
            energy_calc("t", "e")
            energy_calc(False, True)
            energy_calc(False, "t")
            time_calc("t", "e")
            time_calc(False, True)
            time_calc(False, "t")

    def test_maths_raised_errors(self):
        with self.assertRaises(ValueError):
            pythag_hypot("t", "e")
            pythag_hypot(False, True)
            pythag_hypot(False, "t")
            pythag_hypot(-1, "t")
            pythag_leg("t", "e")
            pythag_leg(False, True)
            pythag_leg(False, "t")
            pythag_leg(-1, "t")
            triangle_area("t", "e")
            triangle_area(False, True)
            triangle_area(False, "t")
            triangle_area(-1, "t")
            trapezium_area("t", "e", "s")
            trapezium_area(False, True, False)
            trapezium_area(False, "t", False)
            trapezium_area(False, "t", False)
            circle_area("t")
            circle_area(False)
            circle_area(-1)

if __name__ == '__main__':
    unittest.main()
