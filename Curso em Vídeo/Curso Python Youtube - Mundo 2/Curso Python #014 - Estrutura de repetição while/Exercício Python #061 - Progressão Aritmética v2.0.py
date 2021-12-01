"""https://youtu.be/vu5ehetQGe8
Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de
uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while."""

print('=' * 30)
print('10 PRIMEIROS TERMOS DE UMA PA')
print('=' * 30)
p = int(input('\nPrimeiro termo: '))
r = int(input('Razão: '))
i = 1
while i <= 10:
    print(p, end=', ')
    p += r
    i += 1
print('FIM!')
