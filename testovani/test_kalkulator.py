from unittest import TestCase
from kalkulator import Kalkulator


class TestKalkulator(TestCase):
    def test_to_the_power_of(self):
        calc = Kalkulator()
        self.assertEqual(4, calc.to_the_power_of(2, 2))

    def test_scitani(self):
        calc = Kalkulator()
        self.assertEqual(4, calc.scitani(2, 2))
        self.assertEqual(6, calc.scitani(3, 3))

    def test_odecitani(self):
        calc = Kalkulator()
        self.assertEqual(0, calc.odecitani(2, 2))
        self.assertEqual(-2, calc.odecitani(0, 2))

    def test_nasobeni(self):
        calc = Kalkulator()
        self.assertEqual(4, calc.nasobeni(2, 2))
        self.assertEqual(44, calc.nasobeni(11, 4))

    def test_deleni(self):
        calc = Kalkulator()
        self.assertEqual(1, calc.deleni(2, 2))
        self.assertEqual(0.1, calc.deleni(2, 20))
        self.assertEqual(None, calc.deleni(2, 0))