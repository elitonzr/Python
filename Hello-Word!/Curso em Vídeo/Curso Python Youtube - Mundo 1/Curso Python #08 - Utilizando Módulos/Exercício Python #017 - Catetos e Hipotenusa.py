# Exercício Python 017:
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

# Com o uso de biblioteca.
'''import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
print('\nA hipotenusa vai medir {:.2f}.'.format(math.hypot(co, ca))) '''

# Sem o uso de biblioteca.
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
print('\nA hipotenusa vai medir {:.2f}.'.format((co ** 2 + ca ** 2)**(1/2)))
