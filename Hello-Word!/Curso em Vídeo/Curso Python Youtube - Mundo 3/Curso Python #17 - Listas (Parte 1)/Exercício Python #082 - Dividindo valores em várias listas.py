"""https://youtu.be/uk0gDFQEo_I
Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas
extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o
conteúdo das três listas geradas."""

lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um número: ')))
    res = ' '
    while res not in 'SN':
        res = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if res in 'N':
        break
for pos, item in enumerate(lista):
    if item % 2 == 0:
        par.append(item)
    elif item % 2 == 1:
        impar.append(item)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')