import unittest
import main


class TestEquation(unittest.TestCase):

    def test_equation_1(self):
        self.assertTrue(main.validate_eq(eq_str='5*x^3+2*x'), "Should contain valid equation characters")

    def test_equation_2(self):
        self.assertFalse(main.validate_eq(eq_str='5*x3+ 2*x'), "Should contain Invalid equation characters")

    def test_rangeX_3(self):
        self.assertNotEqual(main.check_user_input('3'), -1, "Should be integer or Float Number")

    def test_rangeX_4(self):
        self.assertEqual(main.check_user_input('3b'), -1, "Shouldn't be integer or Float Number")

    def test_rangeX_5(self):
        self.assertEqual(main.check_user_input('3.8'), 3.8, "Should be Float Number = 3.8")


if __name__ == '__main__':
    unittest.main()
