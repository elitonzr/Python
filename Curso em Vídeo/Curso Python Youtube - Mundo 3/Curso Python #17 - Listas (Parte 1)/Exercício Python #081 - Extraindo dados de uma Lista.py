"""https://youtu.be/SXJKAVVlvGA
Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""

lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    res = ' '
    while res not in 'SN':
        res = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if res in 'N':
        break
print(f'Você digitou {len(lista)} Elementos')
print(f'Os valores em ordem decrescente são: {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
