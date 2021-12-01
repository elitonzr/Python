""" https://youtu.be/ETnExBCFeps
Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
"""

pessoa = dict()
galera = []
soma = media = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: ')).capitalize().strip()
    while True:
        pessoa['Sexo'] = str(input('Sexo [M/F]: ')).capitalize().strip()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F.')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    galera.append(pessoa.copy())
    resp = ' '
    while True:
        resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp in 'N':
        break
print('-='*30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['Sexo'] in 'F':
        print(f'{p["Nome"]}', end=' ')
print()
print(f'D) Lista das pessoas que estão acima da média:')
for p in galera:
    if p['Idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v};', end=' ')
        print()
