"""https://www.youtube.com/watch?v=NZiNphKkxhg
Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou
não formar um triângulo."""

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a <  b + c and a > abs(b - c) and b <  a + c and b > abs(a - c) and c <  b + a and c > abs(b - a):
    print('Os segmentos a cima PODEM FORMAR triângulo!')
else:
    print('Os segmentos a cima NÃO PODEM FORMAR triângulo!')


