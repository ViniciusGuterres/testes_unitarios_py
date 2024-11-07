import unittest
from variacao02 import UtilitariosAnaliseTexto

class TestUtilitariosAnaliseTexto(unittest.TestCase):    
    def setUp(self):
        self.util = UtilitariosAnaliseTexto()
    
    def test_prefixo_comum_basico(self):
        lista_de_palavras = ["flor", "flora", "flop"]
        esperado = "flo"
        self.assertEqual(self.util.prefixo_comum(lista_de_palavras), esperado)

    def test_sem_prefixo_comum(self):
        lista_de_palavras = ["cao", "gato", "jaqueta"]
        esperado = ""
        self.assertEqual(self.util.prefixo_comum(lista_de_palavras), esperado)
    
    def test_palavra_completa_de_prefixo(self):
        lista_de_palavras = ["int", "integer", "integral"]
        esperado = "int"
        self.assertEqual(self.util.prefixo_comum(lista_de_palavras), esperado)
    
    def test_palavras_identicas(self):
        lista_de_palavras = ["test", "test", "test"]
        esperado = "test"
        self.assertEqual(self.util.prefixo_comum(lista_de_palavras), esperado)
    
    def test_lista_vazia(self):
        lista_de_palavras = []
        esperado = ""
        self.assertEqual(self.util.prefixo_comum(lista_de_palavras), esperado)
    
    def test_palavra_unica(self):
        lista_de_palavras = ["solidao"]
        esperado = "solidao"
        self.assertEqual(self.util.prefixo_comum(lista_de_palavras), esperado)
    
    def test_prefixo_comum_parcial(self):
        lista_de_palavras = ["compute", "compatible", "comparison"]
        esperado = "comp"
        self.assertEqual(self.util.prefixo_comum(lista_de_palavras), esperado)

    def test_passando_lista_de_numeros(self):
        numbers_list = [1, 2, 3]
        esperado = ""
        self.assertEqual(self.util.prefixo_comum(numbers_list), esperado)

    def test_prefixo_comum_numerico(self):
        lista_palavras = [12345, 12356, 12378]
        esperado = "123"
        self.assertEqual(self.util.prefixo_comum(lista_palavras), esperado)

    def test_sem_prefixo_comum_numerico(self):
        lista_palavras = [123, 456, 789]
        esperado = ""
        self.assertEqual(self.util.prefixo_comum(lista_palavras), esperado)

    def test_lista_de_tipos_mista(self):
        lista_palavras = [1234, "123abc", 123]
        esperado = "123"
        self.assertEqual(self.util.prefixo_comum(lista_palavras), esperado)

if __name__ == '__main__':
    unittest.main()