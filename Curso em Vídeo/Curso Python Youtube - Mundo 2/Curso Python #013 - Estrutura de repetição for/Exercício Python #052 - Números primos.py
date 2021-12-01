"""https://youtu.be/Er5Hyd4LyVw
Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele
é ou não um número primo."""

i = 0
n = int(input('Digite um número inteiro: '))
for c in range(1, n + 1):
    if n % c == 0:
        i += 1
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end=' ')
print('\n\n\033[mO número {} foi divisível {} vezes'.format(n, i))
if i == 2:
    print('Por isso ele \033[33mÉ PRIMO!')
else:
    pass
    print('Por isso ele \033[31mNÃO É PRIMO!')
