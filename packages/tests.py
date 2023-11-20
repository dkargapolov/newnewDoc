
__all__ = ['TestCalculate','maintest']

"""
Тестирование функции calculate
"""
from .calculations import *
import unittest


class TestCalculate(unittest.TestCase):

    '''class for testing functionality and accuracy of calculations.

    A function test all functions and abilities of calculations.py


    '''

    def test_sum(self):
        self.assertEqual(calculate(1024, 16, '+'), 1040)

    def test_minus(self):
        self.assertEqual(calculate(16, 16, '-'), 0)

    def test_multiply(self):
        self.assertEqual(calculate(4, 3, '*'), 12)

    def test_division(self):
        self.assertEqual(calculate(6, 2, '/'), 3)

    def test_stepen(self):
        self.assertEqual(calculate(2, 2, '**'), 4)

    def test_ostatok(self):
        self.assertEqual(calculate(2, 2, '%'), 0)

    def test_std_dev(self):
        self.assertEqual(calculate([1, 2], 0, 'std_dev'), 0.5)

    def test_convert_precision(self):
        self.assertEqual(calculate(0.000001, 0, 'precision'), 6)

    def test_medium(self):
        self.assertEqual(calculate([1, 2, 3], 0, 'medium'), 2.0)

    def test_variance(self):
        self.assertEqual(calculate([156, 178, 164], 0, 'variance'), 82.66666667)

    def test_median(self):
        self.assertEqual(calculate([1, 1, 2, 4], 0, 'median'), 1.5)


def maintest():
    print(unittest.main())
