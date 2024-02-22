# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template.

import locale
from datetime import datetime
# import json
import string
from pathlib import Path
from urllib.request import CacheFTPHandler

CAMINHO_ARQUIVO = Path(__file__).parent / '20_texto_exemplo.txt'

locale.setlocale(locale.LC_ALL, '')


def converte_para_brl(numero: float) -> str:
    # brl  = 'R$ ' + locale.currency(numero, symbol=False, grouping=True)
    # grouping serve para o separador de milhar
    brl = locale.currency(numero, grouping=True)
    return brl


data = datetime(2024, 2, 14)
dados = dict(
    nome='João',
    valor=converte_para_brl(1_234_456),
    data=data.strftime('%d/%m/%Y'),
    empresa='O. M.',
    telefone='+55 (35) 1234-5678'
)

# print(json.dumps(dados, indent=2, ensure_ascii=False))
# texto = '''
# Prezado(a) $nome,

# Informamos que sua mensalidade será cobrada no valor de ${valor} no dia $data. Caso
# deseje cancelar o serviço, entre em contato com a $empresa pelo telefone $telefone.

# Atenciosamente,

# ${empresa},
# Abraços
# '''


# Para caso deseje mudar o indicador de variavel no texto. NÃO É MTO RECOMEDADO
# class MyTemplate(string.Template):
#     delimiter = '%'


with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
    texto = arquivo.read()
    template = string.Template(texto)
    print(template.substitute(dados))


# safe_substitute utilizada para garatir q se não houver determinada variavel
# no dicionario não tenha erro na execução:
# print(template.safe_substitute(dados))
