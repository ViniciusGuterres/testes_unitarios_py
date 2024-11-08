import unittest
from variacao02 import UtilitariosAnaliseTexto

class TestUtilitariosAnaliseTexto(unittest.TestCase):
    def setUp(self):
         self.texto = "A inteligência artificial pode transformar o futuro da tecnologia."
         self.obj = UtilitariosAnaliseTexto(self.texto)

    def test_palavras_chave_encontradas(self):
        palavras_chaves = ["inteligência", "futuro", "tecnologia"]
        resultado = self.obj.detectar_palavras_chave(palavras_chaves)
        self.assertEqual(resultado, ["inteligência", "futuro", "tecnologia"])

    def test_palavras_chave_nao_detectadas(self):
        palavras = ["carro", "arroz", "feijão"]
        resultado = self.obj.detectar_palavras_chave(palavras)
        self.assertEqual(resultado, [])

    def test_palavras_chave_com_espaco(self):
        palavras = ["inteligência artificial", "futuro", "tecnologia"]
        resultado = self.obj.detectar_palavras_chave(palavras)
        self.assertEqual(resultado, [ "futuro", "tecnologia"])

    def test_palavra_vazia(self):
        resultado = self.obj.detectar_palavras_chave([])
        self.assertEqual(resultado, [])

    def test_anagramas(self):
        self.assertTrue(self.obj.eh_anagrama("listen", "silent"))

    def test_anagramas_com_maiusculas(self):
        self.assertTrue(self.obj.eh_anagrama("Listen", "Silent"))

    def test_anagramas_com_espacos(self):
        self.assertTrue(self.obj.eh_anagrama("a gentleman", "elegant man"))

    def test_nao_anagramas(self):
        self.assertFalse(self.obj.eh_anagrama("hello", "world"))

    def test_palavras_vazias(self):
        self.assertTrue(self.obj.eh_anagrama("", ""))
    
    def test_palavras_mais_comuns(self):
        resultado = self.obj.palavras_mais_comuns(3)
        esperado = {"inteligência": 1, "artificial": 1, "a": 1}
        self.assertEqual(resultado, esperado)

    def test_palavras_comuns_repetidas(self):
        texto = "abacaxi abacaxi abacaxi banana banana"
        obj = UtilitariosAnaliseTexto(texto)
        resultado = obj.palavras_mais_comuns(2)
        esperado = {"abacaxi": 3, "banana": 2}
        self.assertEqual(resultado, esperado)

    def test_palavras_com_acentos(self):
        texto = "café maçã abacaxi maçã"
        obj = UtilitariosAnaliseTexto(texto)
        resultado = obj.palavras_mais_comuns(2)
        esperado = {"maçã": 2, "café": 1}
        self.assertEqual(resultado, esperado)


if __name__ == '__main__':
    unittest.main()