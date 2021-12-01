"""https://youtu.be/EGmlFdwD4C4
Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e
preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a
formatação correta."""

# matriz = [[12, 15, 9], [2, 55, 720], [12, 56, 123]]
matriz = [[[0], [0], [0]], [[0], [0], [0]], [[0], [0], [0]]]
for c in range(0, 3):
    for i in range(0, 3):
        matriz[c][i] = int(input(f'Digite um valor para{c, i}: '))
for c in range(0, len(matriz)):
    for i in range(0, len(matriz)):
        print(f'[{matriz[c][i]:^5}]', end='')
    print()
