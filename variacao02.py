from collections import Counter
import re

class UtilitariosAnaliseTexto:
    def __init__(self,texto):
        self.texto = texto

    def contar_palavras_unicas(self):
        """Conta o número de palavras únicas na string."""
        return len(set(self.texto.lower().split()))

    def frequencia_caracteres(self):
        """Retorna a frequência de cada caractere em um dicionário, ignorando espaços."""
        caracteres = [char.lower() for char in self.texto if char.isalnum()]
        return dict(Counter(caracteres))

    def palavra_mais_longa(self):
        """Retorna a palavra mais longa na string. Em caso de empate, retorna a primeira."""
        palavras = self.texto.split()
        return max(palavras, key=len) if palavras else ""
    
    def detectar_palavras_chave(self, palavras_chave):
        """Retorna as palavras-chave encontradas no texto"""
        palavras_texto = set(re.findall(r'\b\w+\b', self.texto.lower())) 
        palavras_chave_encontradas = [
            palavra for palavra in palavras_chave if palavra.lower() in palavras_texto
        ]
        return palavras_chave_encontradas
    
    def frequencia_palavras(self):
        palavras = re.findall(r'\b\w+\b', self.texto.lower())
        return dict(Counter(palavras))

    def eh_anagrama(self, palavra1, palavra2):
        """Verifica se duas palavras são anagramas entre si, ignorando maiúsculas/minúsculas."""
        palavra1 = re.sub(r'[^a-zA-Z]', '', palavra1).lower()
        palavra2 = re.sub(r'[^a-zA-Z]', '', palavra2).lower()

        return sorted(palavra1.lower()) == sorted(palavra2.lower())

    
    def palavras_mais_comuns(self, n=3):
        """Retorna as `n` palavras mais comuns em um dicionário, incluindo suas frequências."""
        freq_dict = self.frequencia_palavras()
        palavras_ordenadas = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
        return dict(palavras_ordenadas[:n])

    def prefixo_comum(self, lista_palavras):
        """Encontra o prefixo comum mais longo em uma lista de palavras ou números."""
        
        lista_palavras = [str(palavra) for palavra in lista_palavras]
        
        if not lista_palavras:
            return ""
        
        palavra_curta = min(lista_palavras, key=len)

        for i, char in enumerate(palavra_curta):
            if any(palavra[i] != char for palavra in lista_palavras):
                return palavra_curta[:i]
        return palavra_curta
    
    def fatores_primos(self, numero):
        """Retorna uma lista dos fatores primos do número fornecido."""
        fatores = []
        divisor = 2
        
        while numero % divisor == 0:
            fatores.append(divisor)
            numero //= divisor
        
        divisor = 3
        while divisor * divisor <= numero:
            while numero % divisor == 0:
                fatores.append(divisor)
                numero //= divisor
            divisor += 2
        
        if numero > 2:
            fatores.append(numero)
        
        return fatores