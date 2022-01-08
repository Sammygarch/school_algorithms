import unittest

class TestPrivFunc(unittest.TestCase):
    def test_if_not_int_or_float_raise(self):
        with self.assertRaises(ValueError):
            school_algorithms._if_not_int_or_float_raise("hello")
            school_algorithms._if_not_int_or_float_raise(True)
            school_algorithms._if_not_int_or_float_raise(5, True)
            school_algorithms._if_not_int_or_float_raise(True, 5)
            school_algorithms._if_not_int_or_float_raise(1, 5, 5, 2, 3, 4, 5, 6, 4, "hello")
            school_algorithms._if_not_int_or_float_raise(True, "hello")
            school_algorithms._if_not_int_or_float_raise("hello", 5)
            school_algorithms._if_not_int_or_float_raise(["hello", 3, True], 5   )
            school_algorithms._if_not_int_or_float_raise(["hello", 3, True])
            school_algorithms._if_not_int_or_float_raise({"sammy" : 1, "test": True})
            school_algorithms._if_not_int_or_float_raise(("hello", True, 3))
            school_algorithms._if_not_int_or_float_raise(("hello", True, 3))

    def test_if_not_int_or_float_raise_with_int(self):
        try:
            school_algorithms._if_not_int_or_float_raise(5)
            school_algorithms._if_not_int_or_float_raise(5, 5, 4, 3)

        except ValueError:
            assert False, f"'_if_not_int_or_float_raise' raised an exception with an int"

    def test_if_not_int_or_float_raise_with_float(self):
        try:
            school_algorithms._if_not_int_or_float_raise(5.0)
            school_algorithms._if_not_int_or_float_raise(5.0, 3.5, 7.1)

        except ValueError:
            assert False, f"'_if_not_int_or_float_raise' raised an exception with a float"

    def test_if_not_int_or_float_raise_with_float_and_int(self):
        try:
            school_algorithms._if_not_int_or_float_raise(4, 5.0)
            school_algorithms._if_not_int_or_float_raise(4.0, 5)

        except ValueError:
            assert False, f"'_if_not_int_or_float_raise' raised an exception with a float"

class TestPhysicsAlgos(unittest.TestCase):
    def test_power_calc(self):
        self.assertEqual(school_algorithms.power_calc(4, 2), 2.0)

    def test_energy_calc(self):
        self.assertEqual(school_algorithms.energy_calc(4, 2), 8)

    def test_time_calc(self):
        self.assertEqual(school_algorithms.time_calc(2, 4), 2.0)

class TestMathsAlgos(unittest.TestCase):
    def test_pythag_hypot(self):
        self.assertEqual(school_algorithms.pythag_hypot(4, 2), 4.47213595499958)

    def test_pythag_leg(self):
        self.assertEqual(school_algorithms.pythag_leg(7, 2), 6.708203932499369)

    def test_triangle_area(self):
        self.assertEqual(school_algorithms.triangle_area(4, 2), 4.0)

    def test_trapezium_area(self):
        self.assertEqual(school_algorithms.trapezium_area(4, 5, 6), 27.0)

    def test_cirle_area(self):
        self.assertEqual(school_algorithms.circle_area(10), 314.1592653589793)

class TestForRaisedErrors(unittest.TestCase):
    def test_physics_raised_errors(self):
        with self.assertRaises(ValueError):
            school_algorithms.power_calc("t", "e")
            school_algorithms.power_calc(False, True)
            school_algorithms.power_calc(False, "t")
            school_algorithms.energy_calc("t", "e")
            school_algorithms.energy_calc(False, True)
            school_algorithms.energy_calc(False, "t")
            school_algorithms.time_calc("t", "e")
            school_algorithms.time_calc(False, True)
            school_algorithms.time_calc(False, "t")

    def test_maths_raised_errors(self):
        with self.assertRaises(ValueError):
            school_algorithms.pythag_hypot("t", "e")
            school_algorithms.pythag_hypot(False, True)
            school_algorithms.pythag_hypot(False, "t")
            school_algorithms.pythag_leg("t", "e")
            school_algorithms.pythag_leg(False, True)
            school_algorithms.pythag_leg(False, "t")
            school_algorithms.triangle_area("t", "e")
            school_algorithms.triangle_area(False, True)
            school_algorithms.triangle_area(False, "t")
            school_algorithms.trapezium_area("t", "e", "s")
            school_algorithms.trapezium_area(False, True, False)
            school_algorithms.trapezium_area(False, "t", False)
            school_algorithms.circle_area("t")
            school_algorithms.circle_area(False)

if __name__ == '__main__':
    from src.school_algorithms import school_algorithms
    unittest.main()
