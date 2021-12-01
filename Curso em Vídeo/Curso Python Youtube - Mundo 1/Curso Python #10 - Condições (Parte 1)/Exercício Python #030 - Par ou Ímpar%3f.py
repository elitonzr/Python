"""https://www.youtube.com/watch?v=4vFCzKuHOn4&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=41
Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR."""

n = int(input('Digite um número inteiro:'))

if n % 2 == 0:
    print('\nO número {} é PAR.'.format(n))
else:
    print('\nO número {} é ÍMPAR.'.format(n))
