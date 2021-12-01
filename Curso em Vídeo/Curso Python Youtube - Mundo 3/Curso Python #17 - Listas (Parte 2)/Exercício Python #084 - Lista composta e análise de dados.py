"""https://youtu.be/zPtvuLiEdKk
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""

# cadastro = [['Ana', 75.5], ['Pedro', 89], ['Joana', 89], ['Carolina', 55], ['Bianca', 55]]
cadastro = []
dados = []
menorpeso = maiorpeso = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(cadastro) == 0:
        menorpeso = dados[1]
        maiorpeso = dados[1]
    else:
        if dados[1] < menorpeso:
            menorpeso = dados[1]
        if dados[1] > maiorpeso:
            maiorpeso = dados[1]
    cadastro.append(dados[:])
    dados.clear()
    res = ' '
    while res not in 'SN':
        res = str(input('Deseja Continuar [S/N]: ')).strip().upper()[0]
    if res in 'N':
        break
print(f'Total de pessoas cadastradas {len(cadastro)}')
print(f'O maior peso foi de {maiorpeso:.1f}Kg. Peso de ', end='')
for c in cadastro:
    if c[1] == maiorpeso:
        print(f'[{c[0]}] ', end='')
print(f'\nO menor peso foi de {menorpeso:.1f}Kg. Peso de ', end='')
for c in cadastro:
    if c[1] == menorpeso:
        print(f'[{c[0]}] ', end='')
