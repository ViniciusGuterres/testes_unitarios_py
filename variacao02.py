from collections import Counter

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