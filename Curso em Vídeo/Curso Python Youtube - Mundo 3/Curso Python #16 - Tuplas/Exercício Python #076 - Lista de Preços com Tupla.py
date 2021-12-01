"""https://youtu.be/Qp2cXfCHk2I
Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na
sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""

tupla = (
    'Lápis', 1.75,
    'Borracha', 2.00,
    'Caderno', 15.90,
    'Estojo', 25.00,
    'Tranferidor', 4.20,
    'Compasso', 9.99,
    'Mochila', 120.32,
    'Canetas', 22.30,
    'Livros', 34.90,)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇO":^40}')  # 40 Espaços alinhado ao Centro
print('-' * 40)
for pos, item in enumerate(tupla):
    if pos % 2 == 0:
        print(f'{item:.<30}', end='')  # com 30 caracteres
        # print('.' * (30 - len(item)), end='R$ ')
    else:
        print(f'R$ {item:7.2f}')
print('-' * 40)
