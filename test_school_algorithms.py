import unittest

from src.school_algorithms._if_not_valid_raise import (_if_not_int_or_float_raise,
                                                        _if_not_positive_raise,
                                                        _if_not_int_raise)
from src.school_algorithms import (circle_area,
                                   power_calc,
                                   energy_calc,
                                   time_calc,
                                   pythag_leg,
                                   pythag_hypot,
                                   trapezium_area,
                                   triangle_area,
                                   right_rect_pyramid,
                                   epe_calc,
                                   circumference,
                                   circumference2,
                                   square_pyramid,
                                   lcm, lcm_3_nums)


class TestPrivFunc(unittest.TestCase):
    def test_if_not_int_or_float_raise(self):
        a = "t"
        b = True
        c = [1, 3, 4]
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
            _if_not_int_or_float_raise([1, 2, 3])
            _if_not_int_or_float_raise(a, b, c)

    def test_if_not_int_or_float_raise_with_int(self):
        a = 5
        b = 10
        c = 4
        try:
            _if_not_int_or_float_raise(5)
            _if_not_int_or_float_raise(0)
            _if_not_int_or_float_raise(-4)
            _if_not_int_or_float_raise(5, 6)
            _if_not_int_or_float_raise(5, 6, -4)
            _if_not_int_or_float_raise(5, 5, 4, 3)
            _if_not_int_or_float_raise(-5, +5, 40, 23)
            _if_not_int_or_float_raise(a, b, c)

        except ValueError:
            assert False, f"'_if_not_int_or_float_raise' raised an exception with an int"

    def test_if_not_int_or_float_raise_with_float(self):
        a = 5.7
        b = -3.0
        c = 0.0
        try:
            _if_not_int_or_float_raise(5.0)
            _if_not_int_or_float_raise(4.5)
            _if_not_int_or_float_raise(-5.0)
            _if_not_int_or_float_raise(5.7, -6.0)
            _if_not_int_or_float_raise(5.0, 6.3, -5.9)
            _if_not_int_or_float_raise(-5.0, -6.3, -5.9, 7.3)
            _if_not_int_or_float_raise(5.0, 3.5, 7.1)
            _if_not_int_or_float_raise(a, b, c)

        except ValueError:
            assert False, f"'_if_not_int_or_float_raise' raised an exception with a float"

    def test_if_not_int_or_float_raise_with_float_and_int(self):
        a = 7.4
        b = -3.4
        c = 4
        try:
            _if_not_int_or_float_raise(4, 5.0)
            _if_not_int_or_float_raise(-0.00)
            _if_not_int_or_float_raise(-0.0)
            _if_not_int_or_float_raise(4, 7.3, 5.0)
            _if_not_int_or_float_raise(4.5, 5.0, -6)
            _if_not_int_or_float_raise(4.0, 5)
            _if_not_int_or_float_raise(5.0+5)
            _if_not_int_or_float_raise(5.0, 6, -5.9)
            _if_not_int_or_float_raise(a, b, c)

        except ValueError:
            assert False, f"'_if_not_int_or_float_raise' raised an exception with a float"


    def test_if_not_positive_raise(self):
        a = -1
        b = -9
        c = -6.4
        with self.assertRaises(ValueError):
            _if_not_positive_raise(-4)
            _if_not_positive_raise(-4.0)
            _if_not_positive_raise(-4.0, 2)
            _if_not_positive_raise(-4, 5.0, 6)
            _if_not_positive_raise(0.0, -0.0)
            _if_not_positive_raise(-0.5)
            _if_not_positive_raise(a, b, c)

    def test_if_not_positive_raise_for_no_raise(self):
        a = 6.0
        b = 4.5
        c = 7.3
        try:
            _if_not_positive_raise(4)
            _if_not_positive_raise(4.0)
            _if_not_positive_raise(4.0, 2)
            _if_not_positive_raise(6.7, 3.5, 5)
            _if_not_positive_raise(0.001, 0.5, 0.1)
            _if_not_positive_raise(0.1 - 0.01)
            _if_not_positive_raise(-1 + 2)
            _if_not_positive_raise(a, b, c)

        except ValueError:
            assert False, f"'_if_not_positive_raise' raised an exception with a positive number"

    def test_if_not_int_raise_with_int(self):
        a = 7
        b = -3
        c = 4
        try:
            _if_not_int_raise(4, 5)
            _if_not_int_raise(-0)
            _if_not_int_raise(4, 7, 5)
            _if_not_int_raise(4, 5, -6)
            _if_not_int_raise(4, 5)
            _if_not_int_raise(5+5)
            _if_not_int_raise(5, 6, -5)
            _if_not_int_raise(-5, -6, -5)
            _if_not_int_raise(a, b, c)

        except ValueError:
            assert False, f"'_if_not_int_raise' raised an exception with a float"

    def test_if_not_int_raise(self):
        a = 1.3
        b = 9
        c = -6.4
        with self.assertRaises(ValueError):
            _if_not_int_raise("hello")
            _if_not_int_raise("1")
            _if_not_int_raise(True)
            _if_not_int_raise(5, True)
            _if_not_int_raise(True, 5)
            _if_not_int_raise(1, 5, 5, 2, 3, 4, 5, 6, 4, "hello")
            _if_not_int_raise(True, "hello")
            _if_not_int_raise("hello", 5)
            _if_not_int_raise(["hello", 3, True], 5   )
            _if_not_int_raise(["hello", 3, True])
            _if_not_int_raise({"sammy" : 1, "test": True})
            _if_not_int_raise(("hello", True, 3))
            _if_not_int_raise(("hello", True, 3))
            _if_not_int_raise([1, 2, 3])
            _if_not_int_raise(a, b, c)

class TestPhysicsAlgos(unittest.TestCase):
    def test_power_calc(self):
        a, b = 4, 2
        self.assertEqual(power_calc(4, 2), 2.0)
        self.assertEqual(power_calc(-4, 2), -2.0)
        self.assertEqual(power_calc(4.0, 2), 2.0)
        self.assertEqual(power_calc(4.0, 2.0), 2.0)
        self.assertEqual(power_calc(-4.0, 2.0), -2.0)
        self.assertEqual(power_calc(-4.0, -2.0), 2.0)
        self.assertEqual(power_calc(4, -2), -2.0)
        self.assertEqual(power_calc(a, b), 2.0)
        a, b = 4.0, 2.0
        self.assertEqual(energy_calc(a, b), 8)

    def test_energy_calc(self):
        a, b = 2, 4
        self.assertEqual(energy_calc(4, 2), 8)
        self.assertEqual(energy_calc(-4, 2), -8)
        self.assertEqual(energy_calc(4.0, 2), 8)
        self.assertEqual(energy_calc(4.0, 2.0), 8)
        self.assertEqual(energy_calc(-4.0, 2.0), -8)
        self.assertEqual(energy_calc(-4.0, -2.0), 8)
        self.assertEqual(energy_calc(4, -2), -8)
        self.assertEqual(energy_calc(a, b), 8)
        a, b = 2.0, 4.0
        self.assertEqual(energy_calc(a, b), 8)


    def test_time_calc(self):
        a, b = 2, 4
        self.assertEqual(time_calc(2, 4), 2.0)
        self.assertEqual(time_calc(2, -4), -2.0)
        self.assertEqual(time_calc(2, 4.0), 2.0)
        self.assertEqual(time_calc(2.0, 4.0), 2.0)
        self.assertEqual(time_calc(2.0, -4), -2.0)
        self.assertEqual(time_calc(-2.0, -4.0), 2.0)
        self.assertEqual(time_calc(2, -4), -2.0)
        self.assertEqual(time_calc(a, b), 2.0)
        a, b = 2.0, 4.0
        self.assertEqual(time_calc(a, b), 2.0)

    def test_epe_calc(self):
        a, b = 4, 2
        self.assertEqual(epe_calc(5, 10), 250)
        self.assertEqual(epe_calc(10, 10), 500)
        self.assertEqual(epe_calc(10.5, 10), 525)
        self.assertEqual(epe_calc(10.5, 6.5), 221.8125)
        self.assertEqual(epe_calc(10, 10), 500)
        self.assertEqual(epe_calc(a, b), 8)
        a, b = 4.0, 2.0
        self.assertEqual(epe_calc(a, b), 8)


class TestShapeAlgos(unittest.TestCase):
    def test_pythag_hypot(self):
        a, b = 4, 2
        self.assertEqual(pythag_hypot(4, 2), 4.47213595499958)
        self.assertEqual(pythag_hypot(4.0, 2), 4.47213595499958)
        self.assertEqual(pythag_hypot(4.0, 2.0), 4.47213595499958)
        self.assertEqual(pythag_hypot(10, 5), 11.180339887498949)
        self.assertEqual(pythag_hypot(10.5, 5), 11.629703349613008)
        self.assertEqual(pythag_hypot(2, 7), 7.280109889280518)
        self.assertEqual(pythag_hypot(a, b), 4.47213595499958)
        a, b = 4.0, 2.0
        self.assertEqual(pythag_hypot(a, b), 4.47213595499958)

    def test_pythag_leg(self):
        a = 4
        b = 2
        self.assertEqual(pythag_leg(7, 2), 6.708203932499369)
        self.assertEqual(pythag_leg(7.0, 2), 6.708203932499369)
        self.assertEqual(pythag_leg(7.0, 2.0), 6.708203932499369)
        self.assertEqual(pythag_leg(11, 5), 9.797958971132712)
        self.assertEqual(pythag_leg(11, 5), 9.797958971132712)
        self.assertEqual(pythag_leg(a, b), 3.4641016151377544)

    def test_triangle_area(self):
        self.assertEqual(triangle_area(4, 2), 4.0)
        self.assertEqual(triangle_area(4.0, 2), 4.0)
        self.assertEqual(triangle_area(4.0, 2.0), 4.0)
        self.assertEqual(triangle_area(4.5, 2.0), 4.5)

    def test_trapezium_area(self):
        self.assertEqual(trapezium_area(4, 5, 6), 27.0)
        self.assertEqual(trapezium_area(4.0, 5, 6), 27.0)
        self.assertEqual(trapezium_area(4.0, 5.0, 6), 27.0)
        self.assertEqual(trapezium_area(4.0, 5.0, 6.0), 27.0)

    def test_cirle_area(self):
        self.assertEqual(circle_area(10), 314.1592653589793)
        self.assertEqual(circle_area(10.0), 314.1592653589793)
        self.assertEqual(circle_area(2.5), 19.634954084936208)

    def test_right_rect_pyramid(self):
        self.assertEqual(right_rect_pyramid(3, 4, 7), 28.0)
        self.assertEqual(right_rect_pyramid(3.0, 4.4, 7.2), 31.680000000000003)
        self.assertEqual(right_rect_pyramid(10, 5, 6), 100)

    def test_circumference(self):
        self.assertEqual(circumference(5),  31.41592653589793)
        self.assertEqual(circumference(5.0),  31.41592653589793)
        self.assertEqual(circumference(7), 43.982297150257104)
        self.assertEqual(circumference(6.25), 39.269908169872416)

    def test_circumference2(self):
        self.assertEqual(circumference2(10), 31.41592653589793)
        self.assertEqual(circumference2(10.0), 31.41592653589793)
        self.assertEqual(circumference2(14), 43.982297150257104)
        self.assertEqual(circumference2(14.0), 43.982297150257104)
        self.assertEqual(circumference2(12.5), 39.269908169872416)

    def test_square_pyramid(self):
        self.assertEqual(square_pyramid(5, 6), 50)
        self.assertEqual(square_pyramid(4.4, 6), 38.720000000000006)
        self.assertEqual(square_pyramid(4.4, 8), 51.62666666666667)

class TestMathsAlgos(unittest.TestCase):
    def test_lcm(self):
        self.assertEqual(lcm(5, 9), 45)
        self.assertEqual(lcm(10, 10), 10)
        self.assertEqual(lcm(5, 6), 30)
        self.assertEqual(lcm(7, 6), 42)

    def test_3_num_lcm(self):
        self.assertEqual(lcm_3_nums(5, 9, 10), 90)
        self.assertEqual(lcm_3_nums(5, 9, 11), 495)
        self.assertEqual(lcm_3_nums(9, 10, 5), 90)
        self.assertEqual(lcm_3_nums(9, 11, 5), 495)

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

    def test_pythag_raised_errors(self):
        with self.assertRaises(ValueError):
            pythag_hypot("t", "e")
            pythag_hypot(False, True)
            pythag_hypot(False, "t")
            pythag_hypot(-1, "t")
            pythag_leg("t", "e")
            pythag_leg(False, True)
            pythag_leg(False, "t")
            pythag_leg(-1, "t")

    def test_triangle_not_positive_raise(self):
        with self.assertRaises(ValueError):
            triangle_area("t", "e")
            triangle_area(False, True)
            triangle_area(False, "t")
            triangle_area(-1, "t")

    def test_trapezium_not_positive_raise(self):
        with self.assertRaises(ValueError):
            trapezium_area("t", "e", "s")
            trapezium_area(False, True, False)
            trapezium_area(False, "t", False)
            trapezium_area(-4, "t", 6)

    def test_pyramid_raised_errors(self):
        with self.assertRaises(ValueError):
            right_rect_pyramid(False, True, False)
            right_rect_pyramid(False, "t", False)
            right_rect_pyramid(1, "t", 5)
            square_pyramid("t", "e")
            square_pyramid(False, True)
            square_pyramid(False, "t")
            square_pyramid(-1, "t")

    def test_circle_raise_errors(self):
        with self.assertRaises(ValueError):
            circle_area("t")
            circle_area(False)
            circle_area(-1)
            circumference("t")
            circumference(False)
            circumference(-1)
            circumference2("t")
            circumference2(False)
            circumference2(-1)


    def test_maths_raised_errors(self):
        with self.assertRaises(ValueError):
            lcm("t", "e")
            lcm(False, True)
            lcm(False, "t")
            lcm(-1, "t")
            lcm(1.5, 5.5)


    def test_pythag_not_positive_raise(self):
        with self.assertRaises(ValueError):
            pythag_hypot(0, 0)
            pythag_hypot(-0.1, -0.01)
            pythag_hypot(-7, -0.0)
            pythag_hypot(-70000000000, -100000000)
            pythag_leg(0, 0)
            pythag_leg(-0.01, -0.1)
            pythag_leg(-0.0, -7 )
            pythag_leg(-1000000000, -70000000000000 )

    def test_triangle_not_positive_raise(self):
        with self.assertRaises(ValueError):
            triangle_area(0, 0)
            triangle_area(-0.01, -0.1)
            triangle_area(-0.0, -7)
            triangle_area(-10000000000, -70000000000)

    def test_trapezium_not_positive_raise(self):
        with self.assertRaises(ValueError):
            trapezium_area(0, 0, 0)
            trapezium_area(-0.01, -0.1, 0)
            trapezium_area(-0.0, -7, 0)
            trapezium_area(-200000000, -700000, -8.4)

    def test_pyramid_not_positibe_raise(self):
        with self.assertRaises(ValueError):
            right_rect_pyramid(0, 0, 0)
            right_rect_pyramid(-0.01, -0.1, 0)
            right_rect_pyramid(-0.0, -7, 0)
            right_rect_pyramid(-20000, -700000, -100000)
            right_rect_pyramid(20000, 700000, -100000)
            square_pyramid(0, 0)
            square_pyramid(-0.01, -0.1)
            square_pyramid(-0.0, -7)
            square_pyramid(-10000000000, -70000000000)

    def test_circle_not_positibe_raise(self):
        with self.assertRaises(ValueError):
            circle_area(0)
            circle_area(-0.01)
            circle_area(-1)
            circle_area(-100000000000000000)
            circumference(0)
            circumference(-0.01)
            circumference(-1)
            circumference(-100000000000000000)
            circumference2(0)
            circumference2(-0.01)
            circumference2(-1)
            circumference2(-100000000000000000)




    def test_pythag_leg_raise(self):
        with self.assertRaises(ValueError):
            pythag_leg(2, 5)
            pythag_leg(2, 5.7)
            pythag_leg(2.4, 5.7)
            pythag_leg(1.1, 1.2)
            pythag_leg(0.00001, 0.2)


if __name__ == '__main__':
    unittest.main()
