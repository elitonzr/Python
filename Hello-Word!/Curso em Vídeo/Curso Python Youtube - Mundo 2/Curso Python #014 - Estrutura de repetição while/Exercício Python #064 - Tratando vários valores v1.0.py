"""https://youtu.be/mYlbttiLHM0
Exercício Python 064: Crie um programa que leia vários números inteiros pelo
teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a
condição de parada. No final, mostre quantos números foram digitados e qual foi
a soma entre eles (desconsiderando o flag)."""

n = 0
soma = 0
i = 0
n = int(input('Digite um número ou 999 para parar: '))
while n != 999:
    soma += n
    i += 1
    n = int(input('Digite um número ou 999 para parar: '))
print('Foram digitados {} números e a soma entre eles foi {}'.format(i, soma))
