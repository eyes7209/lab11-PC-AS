import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ####### Partner 1
    def test_multiply(self): # 3 assertions
    #     fill in code
        self.assertEqual(mul(1,5), 5)
        self.assertEqual(mul(-2,7), -14)
        self.assertEqual(mul(10, 0), 0)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(5,5),1)
        self.assertAlmostEqual(div(7,10), 0.7)
        self.assertAlmostEqual(div(9,3),3)
    #     fill in code
    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
        with self.assertRaises(ValueError):
            logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(-1,5)
        with self.assertRaises(ValueError):
            logarithm(-1,-1)

    #     fill in code

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypot(3,4),5)
        self.assertEqual(hypot(-5,12), 13)
        self.assertEqual(hypot(-8,-15), -17)
    #     fill in code

    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
        with self.assertRaises(ValueError):
           square_root(-1)
    #     # Test basic function
        self.assertEqual(square_root(4),2)
        self.assertEqual(square_root(100), 10)
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()