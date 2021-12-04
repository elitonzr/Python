'''
https://m.youtube.com/watch?v=kchC5KLZSZ4
Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

from random import randint
from time import sleep

escolhido = randint(0, 5)
print("-=-" * 10)
palpite = int(input("Escolha um número de 0 a 5:\n"))
print("-=-" * 10)
sleep(2)
if palpite == escolhido:
	print("\nParabéns! Você Acertou.")
else:
	print("\nVocê errou! O número escolhido foi {}.".format(escolhido))

