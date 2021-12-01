"""https://youtu.be/-OnqSGh0u4g
Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a
razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
"""

print('=' * 30)
print('10 PRIMEIROS TERMOS DE UMA PA')
print('=' * 30)
p = int(input('\nPrimeiro termo: '))
r = int(input('Razão: '))
decimo = p + (10 - 1) * r
for p in range(p, decimo + 1, r):
    print(p, end=', ')
print('Acabou!')
