"""Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.."""

from math import trunc
num = float(input('Digite um valor: '))
print('\nO Valor digitado foi {} e a sua porção inteira é {}.'.format(num, trunc(num)))


num = float(input('Digite um valor: '))
print('\nO valor digitado foi {} e a sua porção inteira é {}.'.format(num, int(num)))
