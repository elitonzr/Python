# Exercício Python 018:
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians

an = float(input('Digite ãngulo que vocẽ deseja: '))
se = sin(radians(an))
print('\nO ângulo de {} tem o SENO de {:.2f}.'.format(an, se))
co = cos(radians(an))
print('O âangulo de {} tem o COSSENO de {:.2f}'.format(an, co))
tan = tan(radians(an))
print('O ângulo de {} tem a TANGENTE {:.2f}'.format(an, tan))
