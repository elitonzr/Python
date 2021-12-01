""" https://youtu.be/Vsqemzdrj78
Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de
trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente
de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e
acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
from datetime import datetime

dados = {}
dados['Nome'] = str(input('Nome: ')).capitalize().strip()
nascimento = int(input('Ano de Nascimento: '))
dados['Idade'] = datetime.now().year - nascimento
dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['CTPS'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['Idade'] + (dados['contratação'] + 35) - datetime.now().year
print('-='*30)
for k, i in dados.items():
    print(f'- {k} tem o valor {i}')
