import unittest

class TestImports(unittest.TestCase):
    def test_priv_imports(self):
        try:
            from src.school_algorithms._if_not_valid_raise import (_if_not_int_or_float_raise,
                                                                   _if_not_positive_raise,
                                                                   _if_not_int_raise)

        except ImportError:
            assert False, "A private import failed"

    def test_main_imports(self):
        try:
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
                                               lcm,area_of_sector,
                                               kinetic_calc)

        except ImportError:
            assert False, "A main import failed"

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
                                   lcm,area_of_sector,
                                   kinetic_calc)

class TestPrivFuncs(unittest.TestCase):
    def test_if_not_int_or_float_raise(self):
        a, b, c = "t", True, [1, 3, 4]
        with self.assertRaises(ValueError):
            _if_not_int_or_float_raise("hello")
            _if_not_int_or_float_raise("1")
            _if_not_int_or_float_raise(True)
            _if_not_int_or_float_raise(5, True)
            _if_not_int_or_float_raise(True, 5)
            _if_not_int_or_float_raise(1, 5, 5, 2, 3, 4, 5, 6, 4, "hello")
            _if_not_int_or_float_raise(1.5, 5.3, 2.6, 4.3, 5.5, 6.4, "hello")
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
        a, b, c = 5, 10, 4
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
        a, b, c = 5.7, -3.0, 0.0
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
        a, b, c = 7.4, -3.4, 4
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
            a, b, c = 7.40, -3.40, 4.0
            _if_not_int_or_float_raise(a, b, c)

        except ValueError:
            assert False, f"'_if_not_int_or_float_raise' raised an exception with a float"


    def test_if_not_positive_raise(self):
        a, b, c= -1, -9, -6.4
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
        d = int(5.6 + 4.4)
        try:
            _if_not_int_raise(4, 5)
            _if_not_int_raise(-0)
            _if_not_int_raise(4, 7, 5)
            _if_not_int_raise(4, 5, -6)
            _if_not_int_raise(4, 5)
            _if_not_int_raise(d)
            _if_not_int_raise(45)
            _if_not_int_raise(5+5)
            _if_not_int_raise(5, 6, -5)
            _if_not_int_raise(-5, -6, -5)
            _if_not_int_raise(a, b, c)

        except ValueError:
            assert False, f"'_if_not_int_raise' raised an exception with a integer"

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

    def test_kinetic_calc(self):
        a, b = 2, 4
        self.assertEqual(kinetic_calc(10, 5), 250)
        self.assertEqual(kinetic_calc(10, 10), 500)
        self.assertEqual(kinetic_calc(10, 10.5), 525)
        self.assertEqual(kinetic_calc(6.5, 10.5), 221.8125)
        self.assertEqual(kinetic_calc(5, 10), 125)
        self.assertEqual(kinetic_calc(a, b), 8)
        a, b = 2.0, 4.0
        self.assertEqual(kinetic_calc(a, b), 8)


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
        a, b = 4, 2
        self.assertEqual(pythag_leg(7, 2), 6.708203932499369)
        self.assertEqual(pythag_leg(7.0, 2), 6.708203932499369)
        self.assertEqual(pythag_leg(7.0, 2.0), 6.708203932499369)
        self.assertEqual(pythag_leg(11, 5), 9.797958971132712)
        self.assertEqual(pythag_leg(11, 5), 9.797958971132712)
        self.assertEqual(pythag_leg(a, b), 3.4641016151377544)

    def test_triangle_area(self):
        a, b = 4, 2
        self.assertEqual(triangle_area(4, 2), 4.0)
        self.assertEqual(triangle_area(4.0, 2), 4.0)
        self.assertEqual(triangle_area(4.0, 2.0), 4.0)
        self.assertEqual(triangle_area(4.5, 2.0), 4.5)
        self.assertEqual(triangle_area(a, b), 4.0)

    def test_trapezium_area(self):
        a, b, c = 4, 5, 6
        self.assertEqual(trapezium_area(4, 5, 6), 27.0)
        self.assertEqual(trapezium_area(4.0, 5, 6), 27.0)
        self.assertEqual(trapezium_area(4.0, 5.0, 6), 27.0)
        self.assertEqual(trapezium_area(4.0, 5.0, 6.0), 27.0)
        self.assertEqual(trapezium_area(a, b, c), 27.0)

class TestCircleAlgos(unittest.TestCase):
    def test_cirle_area(self):
        a = 10
        self.assertEqual(circle_area(10), 314.1592653589793)
        self.assertEqual(circle_area(10.0), 314.1592653589793)
        self.assertEqual(circle_area(2.5), 19.634954084936208)
        self.assertEqual(circle_area(2.50), 19.634954084936208)
        self.assertEqual(circle_area(a), 314.1592653589793)

    def test_area_of_sector(self):
        a, b = 5, 40
        self.assertEqual(area_of_sector(5, 40), 8.726646259971647)
        self.assertEqual(area_of_sector(5.0, 40.0), 8.726646259971647)
        self.assertEqual(area_of_sector(10, 0.1), 0.08726646259971647)
        self.assertEqual(area_of_sector(10.0, 0.1), 0.08726646259971647)
        self.assertEqual(area_of_sector(a, b), 8.726646259971647)


    def test_circumference(self):
        a = 5
        self.assertEqual(circumference(5),  31.41592653589793)
        self.assertEqual(circumference(5.0),  31.41592653589793)
        self.assertEqual(circumference(7), 43.982297150257104)
        self.assertEqual(circumference(7.0), 43.982297150257104)
        self.assertEqual(circumference(a),  31.41592653589793)

    def test_circumference2(self):
        a = 10
        self.assertEqual(circumference2(10), 31.41592653589793)
        self.assertEqual(circumference2(10.0), 31.41592653589793)
        self.assertEqual(circumference2(14), 43.982297150257104)
        self.assertEqual(circumference2(14.0), 43.982297150257104)
        self.assertEqual(circumference2(a), 31.41592653589793)


class TestPyramidAlgos(unittest.TestCase):
    def test_square_pyramid(self):
        a, b = 5, 6
        self.assertEqual(square_pyramid(5, 6), 50)
        self.assertEqual(square_pyramid(4.4, 6), 38.720000000000006)
        self.assertEqual(square_pyramid(4.4, 8), 51.62666666666667)
        self.assertEqual(square_pyramid(5, 27), 225)
        self.assertEqual(square_pyramid(a, b), 50)


    def test_right_rect_pyramid(self):
        a, b, c = 3, 4, 7
        self.assertEqual(right_rect_pyramid(3, 4, 7), 28)
        self.assertEqual(right_rect_pyramid(3.0, 4.0, 7.0), 28)
        self.assertEqual(right_rect_pyramid(3.0, 4.4, 7.2), 31.680000000000003)
        self.assertEqual(right_rect_pyramid(10, 5, 6), 100)
        self.assertEqual(right_rect_pyramid(a, b, c), 28)

class TestLcmAlgos(unittest.TestCase):
    def test_lcm_1_nums(self):
        a = 7
        self.assertEqual(lcm(5), 5)
        self.assertEqual(lcm(10), 10)
        self.assertEqual(lcm(36), 36)
        self.assertEqual(lcm(6), 6)
        self.assertEqual(lcm(a), 7)

    def test_lcm_2_nums(self):
        a, b = 7, 6
        self.assertEqual(lcm(5, 9), 45)
        self.assertEqual(lcm(10, 10), 10)
        self.assertEqual(lcm(5, 6), 30)
        self.assertEqual(lcm(7, 6), 42)
        self.assertEqual(lcm(a, b), 42)

    def test_3_num_lcm(self):
        a, b, c = 9, 11, 5
        self.assertEqual(lcm(5, 9, 10), 90)
        self.assertEqual(lcm(5, 9, 11), 495)
        self.assertEqual(lcm(12, 15, 75), 300)
        self.assertEqual(lcm(13, 43, 65), 2795)
        self.assertEqual(lcm(a, b, c), 495)

    def test_4_num_lcm(self):
        a, b, c, d = 5, 10, 15, 20
        self.assertEqual(lcm(5, 9, 10, 15), 90)
        self.assertEqual(lcm(5, 9, 10, 16), 720)
        self.assertEqual(lcm(12, 9, 10, 16), 720)
        self.assertEqual(lcm(13, 43, 65, 52), 11180)
        self.assertEqual(lcm(a, b, c, d), 60)

    def test_5_num_lcm(self):
        a, b, c, d, e = 5, 10, 15, 20, 30
        self.assertEqual(lcm(5, 9, 10, 15, 16), 720)
        self.assertEqual(lcm(5, 9, 10, 16, 23), 16560)
        self.assertEqual(lcm(12, 13, 15, 75, 20), 3900)
        self.assertEqual(lcm(5, 10, 15, 20, 30), 60)
        self.assertEqual(lcm(a, b, c, d, e), 60)


class TestForPhysicsRaisedErrors(unittest.TestCase):
    def test_power_calc_raised_errors(self):
        with self.assertRaises(ValueError):
            a, b = False, "t"
            power_calc("t", "e")
            power_calc(False, True)
            power_calc(False, "t")
            power_calc(a, b)

    def test_energy_calc_raised_errors(self):
        with self.assertRaises(ValueError):
            a, b = False, "t"
            energy_calc("t", "e")
            energy_calc(False, True)
            energy_calc(False, "t")
            energy_calc(a, b)

    def test_time_calc_raised_errors(self):
        with self.assertRaises(ValueError):
            a, b = False, "t"
            time_calc("t", "e")
            time_calc(False, True)
            time_calc(False, "t")
            time_calc(a, b)

class TestForPythagRaisedErrors(unittest.TestCase):
    def test_pythag_hypot_raised_errors(self):
        with self.assertRaises(ValueError):
            a, b = -1, "t"
            pythag_hypot("t", "e")
            pythag_hypot(False, True)
            pythag_hypot(False, "t")
            pythag_hypot(-1, "t")
            pythag_hypot(a, b)

    def test_pythag_leg_raised_errors(self):
        with self.assertRaises(ValueError):
            a, b = -1, "t"
            pythag_leg("t", "e")
            pythag_leg(False, True)
            pythag_leg(False, "t")
            pythag_leg(-1, "t")
            pythag_leg(a, b)

class TestForCicleRaisedErrors(unittest.TestCase):
    def test_circle_area_raise_errors(self):
        with self.assertRaises(ValueError):
            a = -1
            circle_area("t")
            circle_area(False)
            circle_area(-34)
            circle_area(0)
            circle_area(a)

    def test_circumference_raise_errors(self):
        with self.assertRaises(ValueError):
            a = -1
            circumference("t")
            circumference(False)
            circumference(-34)
            circumference(0)
            circumference(a)

    def test_circumference2_raise_errors(self):
        with self.assertRaises(ValueError):
            a = -1
            circumference2("t")
            circumference2(False)
            circumference2(-34)
            circumference2(0)
            circumference2(a)

class TestForPyramidRaisedErrors(unittest.TestCase):
    def test_right_rect_pyramid_raised_errors(self):
        with self.assertRaises(ValueError):
            a, b, c = 1, "t", 5
            right_rect_pyramid(False, True, False)
            right_rect_pyramid(False, "t", False)
            right_rect_pyramid(1, "t", 5)
            right_rect_pyramid(0, 0, 0)
            right_rect_pyramid(a, b ,c)

    def test_square_pyramid_raised_errors(self):
        with self.assertRaises(ValueError):
            a, b = -1, "t"
            square_pyramid("t", "e")
            square_pyramid(False, True)
            square_pyramid(False, "t")
            square_pyramid(-1, "t")
            square_pyramid(a, b)

class TestForTrapeziumRaisedErrors(unittest.TestCase):
    def test_trapezium_not_positive_raise(self):
        with self.assertRaises(ValueError):
            a, b, c = -4, "t", 6
            trapezium_area("t", "e", "s")
            trapezium_area(False, True, False)
            trapezium_area(False, "t", False)
            trapezium_area(-4, "t", 6)
            trapezium_area(a, b, c)

class TestForTriangleRaisedErrors(unittest.TestCase):
    def test_triangle_not_positive_raise(self):
        with self.assertRaises(ValueError):
            a, b = -1, "t"
            triangle_area("t", "e")
            triangle_area(False, True)
            triangle_area(False, "t")
            triangle_area(-1, "t")
            triangle_area(a, b)

class TestForLcmRaisedErrors(unittest.TestCase):
    def test_lcm_1_num_raised_errors(self):
        with self.assertRaises(ValueError):
            a = 1.5
            lcm("t")
            lcm(False)
            lcm(-1)
            lcm(True)
            lcm(a)

    def test_lcm_2_nums_raised_errors(self):
        with self.assertRaises(ValueError):
            a, b = 1.5, 5.5
            lcm("t", "e")
            lcm(False, "t")
            lcm(-1, "t")
            lcm(1.5, 5.5)
            lcm(a, b)


    def test_lcm_3_nums_raised_errors(self):
        with self.assertRaises(ValueError):
            a, b, c = 1.5, 5.5, 5.98
            lcm("t", "e", "s")
            lcm(False, True, False)
            lcm(1.5, 5.5, 5.98)
            lcm(1.5, "t", 5.98)
            lcm(a, b, c)

    def test_lcm_4_nums_raised_errors(self):
        with self.assertRaises(ValueError):
            a, b, c, d = 1.5, 5.5, 5.98, 4.5
            lcm("t", "e", "s", "t")
            lcm(False, True, False, 5)
            lcm(False, "t", "5", 1)
            lcm(-1, "t", True, False)
            lcm(1.5, 5.5, 5.98, 4.5)
            lcm(a, b, c, d)

    def test_lcm_5_nums_raised_errors(self):
        with self.assertRaises(ValueError):
            a, b, c, d, e = 1.5, 5.5, 5.98, 4.5, 7.8
            lcm("t", "e", "s", "t", "i")
            lcm(False, True, False, 5, 0)
            lcm(False, "t", "5", 1, True)
            lcm(-1, "t", True, False, "e")
            lcm(1.5, 5.5, 5.98, 4.5, 4)
            lcm(a, b, c, d, e)

class TestForPythagRaisedErrors(unittest.TestCase):
    def test_pythag_hypot_not_positive_raise(self):
        with self.assertRaises(ValueError):
            a, b = 70000000000, -100000000
            pythag_hypot(0, 0)
            pythag_hypot(-0.1, -0.01)
            pythag_hypot(-7, -0.0)
            pythag_hypot(-70000000000, -100000000)
            pythag_hypot(70000000000, -100000000)
            pythag_hypot(a, b)

    def test_pythag_leg_not_positive_raise(self):
        with self.assertRaises(ValueError):
            a, b = 70000000000, -100000000
            pythag_leg(0, 0)
            pythag_leg(-0.01, -0.1)
            pythag_leg(-0.0, -7 )
            pythag_leg(-1000000000, -70000000000000 )
            pythag_leg(1000000000, -70000000000000)
            pythag_hypot(a, b)

    def test_pythag_leg_raise(self):
        with self.assertRaises(ValueError):
            a, b = 2, 5
            pythag_leg(2, 5)
            pythag_leg(2, 5.7)
            pythag_leg(2.4, 5.7)
            pythag_leg(1.1, 1.2)
            pythag_leg(0.00001, 0.2)
            pythag_leg(0.9999999999999999999999, 1)
            pythag_leg(a, b)

class TestForTriangleRaisedErrors(unittest.TestCase):
    def test_triangle_not_positive_raise(self):
        with self.assertRaises(ValueError):
            a, b = 0, 0
            triangle_area(0, 0)
            triangle_area(-0.01, -0.1)
            triangle_area(-0.0, -7)
            triangle_area(-10000000000, -70000000000)
            triangle_area(10000000000, -70000000000)
            triangle_area(a, b)

class TestForTrapeziumRaisedErrors(unittest.TestCase):
    def test_trapezium_not_positive_raise(self):
        with self.assertRaises(ValueError):
            a, b, c = 0, 0, 0
            trapezium_area(0, 0, 0)
            trapezium_area(-0.01, -0.1, 0)
            trapezium_area(-0.0, -7, 0)
            trapezium_area(-200000000, -700000, -8.4)
            trapezium_area(200000000, 700000, -8.4)
            trapezium_area(a, b ,c)

class TestForPyramidRaisedErrors(unittest.TestCase):
    def test_right_rect_pyramid_not_positive_raise(self):
        with self.assertRaises(ValueError):
            a, b, c = 0, 0, 0
            right_rect_pyramid(0, 0, 0)
            right_rect_pyramid(-0.01, -0.1, 0)
            right_rect_pyramid(-0.0, -7, 0)
            right_rect_pyramid(-20000, -700000, -100000)
            right_rect_pyramid(20000, 700000, -100000)
            right_rect_pyramid(a, b, c)

    def test_square_pyramid_not_positive_raise(self):
        with self.assertRaises(ValueError):
            a, b = 0, 0
            square_pyramid(0, 0)
            square_pyramid(-0.01, -0.1)
            square_pyramid(-0.0, -7)
            square_pyramid(-10000000000, -70000000000)
            square_pyramid(-0.0, 5)
            square_pyramid(a, b)

class TestForCircleRaisedErrors(unittest.TestCase):
    def test_circle_area_not_positive_raise(self):
        with self.assertRaises(ValueError):
            a = 0
            circle_area(0)
            circle_area(-0.01)
            circle_area(-1)
            circle_area(-100000000000000000)
            circle_area(-0.0)
            circle_area(a)

    def test_circumference_positive_raise(self):
        with self.assertRaises(ValueError):
            a = 0
            circumference(0)
            circumference(-0.01)
            circumference(-1)
            circumference(-100000000000000000)
            circumference(-0.0)
            circumference(a)

    def test_circumference2_positive_raise(self):
        with self.assertRaises(ValueError):
            a = 0
            circumference2(0)
            circumference2(-0.01)
            circumference2(-1)
            circumference2(-100000000000000000)
            circumference2(-0.0)
            circumference2(a)

if __name__ == '__main__':
    unittest.main()
