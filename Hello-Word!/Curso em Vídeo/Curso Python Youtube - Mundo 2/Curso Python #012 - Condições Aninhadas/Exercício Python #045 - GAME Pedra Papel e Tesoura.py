"""https://www.youtube.com/watch?v=tapTa6KVG-A
Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você."""

from random import choice
from time import sleep

lista = ['PEDRA', 'PAPEL', 'TESOURA']
c = choice(lista)
print('Suas opções:')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
e = int(input('Qual é a sua jogada? '))

if e == 0:
    a = 'PEDRA'
elif e == 1:
    a = 'PAPEL'
elif e == 2:
    a = 'TESOURA'
else:
    a = ''
    print('Opção invalida, tente novamente!')

if a != '':
    sleep(0.2)
    print('\nJO')
    sleep(0.2)
    print('KEN')
    sleep(0.2)
    print('PO!!!')
    print('\nVocê escolheu {} o Computador {}.'.format(a, c))
if c == a:
    print('EMPATE')
elif a == 'PEDRA' and c == 'PAPEL' or a == 'PAPEL' and c == 'TESOURA' or a == 'TESOURA' and c == 'PEDRA':
    print('VOCÊ PERDEU!')
elif c == 'PEDRA' and a == 'PAPEL' or c == 'PAPEL' and a == 'TESOURA' or c == 'TESOURA' and a == 'PEDRA':
    print('VOCÊ VENCEU!')
