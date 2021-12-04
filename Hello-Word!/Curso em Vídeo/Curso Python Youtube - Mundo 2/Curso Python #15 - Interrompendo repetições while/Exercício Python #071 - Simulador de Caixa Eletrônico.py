""" https://youtu.be/_XGgwltYpYk
Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao
usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão
entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
RED         =   "\033[1;31m"
BLUE        =   "\033[1;34m"
YELLOW      =   "\033[1;33m"
CYAN        =   "\033[1;36m"
GREEN       =   "\033[0;32m"
RESET       =   "\033[0;0m"
BOLD        =   "\033[;1m"
REVERSE     =   "\033[;7m"
"""

print('\033[1;33m')
print('-' * 30)
print('         BANCO PYTHON')
print('-' * 30)
print('\033[0;00m')
ced = 50
valor = int(input('Qual será o valor a ser sacado? R$'))
totalced = 0
while True:
    if valor >= ced:
        valor -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'{totalced} Cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if valor == 0:
            break
