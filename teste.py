import unittest

from cal import somar, subtrair, multiplicar, dividir


class TestCalculadora(unittest.TestCase):

    def test_somar(self):
        self.assertEqual(somar(0, 16), 16)

    def test_subtrair(self):
        self.assertEqual(subtrair(0, 4), -4)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(7, 9), 63)

    def test_dividir(self):
        self.assertEqual(dividir(47, 4), 11.75)

    def test_divisao_por_zero(self):
        with self.assertRaises(ZeroDivisionError):
            dividir(10, 0)


if __name__ == "__main__":
    unittest.main()
