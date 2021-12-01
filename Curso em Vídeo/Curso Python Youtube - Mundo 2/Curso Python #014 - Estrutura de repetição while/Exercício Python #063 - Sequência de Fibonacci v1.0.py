"""https://youtu.be/w7yn1_Mfu0E
Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer
e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8"""

print('-' * 30)
print('     Sequência de Fibonacci')
print('-' * 30)
t = int(input('Quantos termos você quer mostrar? '))
a = 0
b = 1
print('{}, {}, '.format(a, b), end='')
while t > 2:
    c = a + b
    a = b
    b = c
    t -= 1
    print('{}, '.format(c), end='')
print('FIM', end='')
