import unittest
from variacao02 import UtilitariosAnaliseTexto

class Teste(unittest.TestCase):
    
    def setUp(self):
        
        self.texto = "azul amarelo"
        
        self.obj = UtilitariosAnaliseTexto(self.texto)

    def test_contar_palavras_unicas(self):
        resultado = self.obj.contar_palavras_unicas()
        
        self.assertEqual(resultado, 2)

    def test_frequencia_caracteres(self):
        resultado = self.obj.frequencia_caracteres()
        esperado = {
            'a':3,
            'z':1,
            'u':1,
            'l':2,
            'm':1,
            'r':1,
            'e':1,
            'o':1    
        }
        self.assertEqual(resultado, esperado)

    def test_palavra_mais_longa(self):
        resultado = self.obj.palavra_mais_longa()
        self.assertEqual(resultado, "amarelo")  

if __name__ == '__main__':
    unittest.main()
