import pytest
from apps.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calc(self):
        assert self.calc.multiply(self,2,2) == 4

    def test_division_cals(self):
        assert self.calc.division(self,25,5) == 5

    def test_adding_calc(self):
        assert self.calc.adding(self,111,222) == 333

    def test_subtraction_calc(self):
        assert self.calc.subtraction(self,20,5) == 15
