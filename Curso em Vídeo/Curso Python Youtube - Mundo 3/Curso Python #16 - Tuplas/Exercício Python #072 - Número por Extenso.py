"""https://youtu.be/ei2Kr3ccfO0
Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero
até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso."""

e = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
     'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
     'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
     'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
     'Dezenove', 'Vinte')
op = 'S'
while op == 'S':
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if 0 <= n <= 20:
            break
        print('Tente novamente!', end='')
    print(f'\nVocê digitou o número \033[33m{e[n]}\033[00m')
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja contonuar [S/N]: ')).strip().upper()[0]
