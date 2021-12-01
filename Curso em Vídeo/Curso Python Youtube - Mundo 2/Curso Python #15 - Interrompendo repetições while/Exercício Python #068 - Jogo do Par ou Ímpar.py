""" https://youtu.be/EIzgKCCDdc0
Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""

from random import randint

i = 0
print('-*-' * 10)
print('     JOGO DO PAR OU ÍMPAR')
print('-*-' * 10)
while True:
    n = int(input('\nDiga um valor: '))
    c = randint(0, 11)
    j = ' '
    while j not in 'PI':
        j = str(input('Escolha Par ou Ímpar [P/I]: ')).upper().strip()[0]
    soma = (n + c)
    print(f'Você escolheu {n} e o computador {c}. Total de {soma} ', end='')
    if soma % 2 == 0:
        print('DEU PAR')
        if j == 'P':
            print('Você Ganhou!')
            i += 1
        else:
            print('Você Perdeu!')
            break
    else:
        print('DEU ÍMPAR')
        if j == 'I':
            print('Você Ganhou!')
            i += 1
        else:
            print('Você Perdeu!')
            break
print(f'GAME OVER! Você venceu {i} vezes.')
