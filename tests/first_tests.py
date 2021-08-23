import pytest

from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calc_correct(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_div_calc_correct(self):
        assert self.calc.division(self, 6, 2) == 3

    def test_add_calc_correct(self):
        assert self.calc.adding(self, 5, 3) == 8

    def test_sub_calc_correct(self):
        assert self.calc.subtraction(self, 7, 2) == 5
