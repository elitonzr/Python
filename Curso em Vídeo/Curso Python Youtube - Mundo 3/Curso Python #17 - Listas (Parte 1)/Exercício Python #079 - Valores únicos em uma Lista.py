"""https://youtu.be/LkAzRnc_GPk
Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
em ordem crescente."""

lista = list()
while True:
    numero = int(input('Digite um numero: '))
    if numero in lista:
        print('Valor Duplicado! Não sera adicionado.')
    else:
        lista.append(numero)
        print('Valor adicionado com sucesso!')
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if r in 'N':
        break
print(f'Os valores digitados em ordem crescente foram: {sorted(lista)}')
