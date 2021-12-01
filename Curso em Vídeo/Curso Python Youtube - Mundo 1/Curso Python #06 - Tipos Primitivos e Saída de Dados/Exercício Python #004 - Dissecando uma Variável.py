"""https://youtu.be/tHYxjJxtJko Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o
seu tipo primitivo e todas as informações possíveis sobre ele. """

a = input('Digite algo: ')
print('O tipo primitivo desse valor é {}'.format(type(a)))
print('Só tem espaços? {}'.format(a.isspace()))
print('É um número? {}'.format(a.isnumeric()))
print('É alfabético? {}'.format(a.isalpha()))
print('É alfanumérico? {}'.format(a.isalnum()))
print('Está em maiúsculas? {}'.format(a. isupper()))
print('Esta em minúscula? {}'.format(a.islower()))
print('Esta capitalizada? {}'.format(a.istitle()))
