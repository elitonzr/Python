"""https://youtu.be/mlwt2CRQkTQ
Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""
from random import randint
menor = 0
maoir = 0
n = (randint(1, 10),
     randint(1, 10),
     randint(1, 10),
     randint(1, 10),
     randint(1, 10))
print('Os valores sorteados foram: ', end='')
for c in n:
    print(f'{c} ', end='')
for pos, item in enumerate(n):
    if pos == 0:
        menor = item
        maoir = item
    else:
        if menor > item:
            menor = item
        if maoir < item:
            maoir = item
print(f'\n\nO maoir valor sorteado foi {maoir}')
print(f'O menor valor sorteado foi {menor}')

print(f'\nO maoir valor sorteado foi {max(n)}')
print(f'O menor valor sorteado foi {min(n)}')
