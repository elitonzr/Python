""" https://youtu.be/4Ca6iRJo3M0
Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o
programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
"""

th = mm = maior = 0
while True:
    print('-' * 30)
    print('     Cadastre uma pessoa')
    print('-' * 30)
    print('-' * 30)
    sexo = ' '
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().  strip()[0]
    print(f'\33[1;36mPessoa cadastrada: {idade} anos do sexo {sexo}.\33[0;0m')
    print('-' * 30)
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        th += 1
    elif sexo == 'F' and idade < 20:
        mm += 1
    op = ' '
    while op not in 'SN':
        op = str(input('\33[1;31mDeseja continuar [S/N]: \33[0;0m')).upper().strip()[0]
    if op == 'N':
        break
print(f'\n\33[1;32m{maior} Pessoas com mais 18 anos')
print(f'{th} homens cadastrados')
print(f'{mm} Mulheres com menos de 20 anos')
