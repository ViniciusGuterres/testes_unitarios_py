import unittest
from variacao02 import UtilitariosAnaliseTexto

class TestUtilitariosAnaliseTexto(unittest.TestCase):
    def setUp(self):
        self.util = UtilitariosAnaliseTexto("")
    
    def test_fatores_primos(self):
        numero = 13
        esperado = [13]
        self.assertEqual(self.util.fatores_primos(numero), esperado)

    def test_fatores_primos_numero_composto(self):
        numero = 28
        esperado = [2, 2, 7]
        self.assertEqual(self.util.fatores_primos(numero), esperado)

    def test_fatores_primos_multiplo_fatores_repetidos(self):
        numero = 60
        esperado = [2, 2, 3, 5]
        self.assertEqual(self.util.fatores_primos(numero), esperado)

    def test_fatores_primos_numero_um(self):
        numero = 1
        esperado = []
        self.assertEqual(self.util.fatores_primos(numero), esperado)

    def test_fatores_primos_numero_grande(self):
        numero = 97
        esperado = [97]
        self.assertEqual(self.util.fatores_primos(numero), esperado)

    def test_fatores_primos_quadrado_do_numero_primo(self):
        numero = 49
        esperado = [7, 7]
        self.assertEqual(self.util.fatores_primos(numero), esperado)

if __name__ == '__main__':
    unittest.main()