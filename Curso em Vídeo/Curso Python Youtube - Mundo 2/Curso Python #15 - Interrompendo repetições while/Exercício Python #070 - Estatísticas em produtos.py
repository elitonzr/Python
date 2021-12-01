""" https://youtu.be/hS8QdW-1HTo
Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
"""

produto = ' '
total = tprodcaro = prodmbvalor = 0
prodmb = ' '
print('\33[1;33m')
print('-' * 30)
print('     CADASTRO DE PRODUTOS')
print('-' * 30)
print('\33[0;00m')
while True:
    print('-' * 30)
    newprod = str(input("Nome do Produto: ")).strip()
    newprodvalor = float(input('Preço: R$ '))
    total += newprodvalor
    print('-' * 30)
    if newprodvalor > 1000:
        tprodcaro += 1
    if prodmbvalor == 0 or prodmbvalor > newprodvalor:
        prodmb = newprod
        prodmbvalor = newprodvalor
    op = ' '
    while op not in 'SN':
        op = str(input('\n\33[1;31mDeseja continuar [S/N]: \33[0;0m')).upper().strip()[0]
    if op == 'N':
        break
print(f'\n\33[1;32mTotal da compra:\33[1;31m R${total:.2f}')
print(f'\33[1;32mTotal de produtos acima de R$1000:\33[1;31m {tprodcaro}')
print(f'\33[1;32mProduto mais barato:\33[1;31m {prodmb} que custa R${prodmbvalor:.2f}')
