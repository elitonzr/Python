"""https://www.youtube.com/watch?v=ZX7sCPjcHA0
Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo
será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes"""

a = float(input('Primeiro seguimento: '))
b = float(input('Segundo seguimento: '))
c = float(input('Terceiro seguimento: '))

if b + c > a > abs(b - c) and a + c > b > abs(a - c) and b + a > c > abs(b - a):
    print('Os segmentos acima PODEM FORMAR um ', end='')
    if a == b == c:
        print('triângulo EQUILÁTERO: todos os lados iguais!')
    elif a != b and a != c and b != c:
        print('triângulo ESCALENO: todos os lados diferentes!')
    else:
        print('triângulo ISÓSCELES: dois lados iguais, um diferente')
else:
    print('Não é possível Formar um triângulo!')
