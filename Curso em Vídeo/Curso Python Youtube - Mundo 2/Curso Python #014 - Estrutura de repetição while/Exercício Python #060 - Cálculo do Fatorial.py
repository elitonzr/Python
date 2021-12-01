"""https://youtu.be/9dlBZlkvvxY
Exercício Python 060: Faça um programa que leia um número qualquer e mostre o
seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120"""

n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando com while {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)
f = 1
print('\nCalculando com for {}! = '.format(n), end='')
for i in range(n, 0, -1):
    print('{}'.format(i), end='')
    print(' x ' if i > 1 else ' = ', end='')
    f *= i
print(f)
