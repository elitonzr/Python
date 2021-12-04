"""https://youtu.be/IL5iBWoKRIs
Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
ainda não atingiram a maioridade e quantas já são maiores.
"""

from datetime import date
atual = date.today().year
maior = menor = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    idade = atual - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('\nAo todo tivemos {} pessoas maiores de idade'.format(maior))
print('E também tivemos {} pessoas menores de idade'.format(menor))
