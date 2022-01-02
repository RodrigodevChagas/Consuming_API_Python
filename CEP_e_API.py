# Importando as bibliotecas que serão usadas no projeto.
import re
import requests

# Criando a classe que vai validar, formatar e acessar uma API para trabalhar com informações adcionais
class Busca_Endereco:

#region - Fazendo a validação do CEP e retornando um erro, caso seja inválido.
    def __init__(self, numero):
        if len(numero) == 8:
            if self.valida_cep(numero):
                self._numero = numero
            else:
                raise ValueError('CEP inválido.')
        else:
            raise ValueError('CEP inválido.')
#endregion

#region - Função que faz a validação do CEP usando RegEx.
    def valida_cep(self, numero):

        padrao = '([0-9]{5})([0-9]{3})'
        valida = re.search(padrao, numero)

        if valida:
            return True
        else:
            return False
#endregion

#region - Encapsulamento usando um getter (property).
    @property
    def numero(self):
        return self._numero
#endregion

#region - Função que cria uma máscara para a formatação do número do CEP.
    def cep_mask(self):
        padrao = '([0-9]{5})([0-9]{3})'
        valida = re.search(padrao, self.numero)
        mascara = f'{valida.group(1)}-{valida.group(2)}'
        return mascara
#endregion

#region - Usando o método __str__ para retornar a máscara
    def __str__(self):
        return self.cep_mask()
#endregion

# - Função que acessa uma API para informações adcionais sobre o CEP, como logradouro, bairro, localidade e UF.
    def acessa_api(self):
        url = f"https://viacep.com.br/ws/{self.numero}/json/"
        r = requests.get(url)
        dados = r.json()

        return (
            dados['logradouro'],
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )

