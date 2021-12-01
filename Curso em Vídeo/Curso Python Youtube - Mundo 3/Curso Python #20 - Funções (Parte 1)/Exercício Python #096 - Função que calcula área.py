"""https://youtu.be/oV1s53YGtvE
Exercício Python 096: Faça um programa que tenha uma função chamada área(), que
receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área
do terreno."""


def area(larg, comp):
    a = larg * comp
    print()
    print('-' * 40)
    print(f'A área de um terreno {larg}m x {comp}m é de: {a:.1f}m²')
    print('-' * 40)


print('-=' * 20)
print(f'{"Calcula área de um terreno":^40}')
print('-=' * 20)
l = float(input('\nLargura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
