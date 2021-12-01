"""https://youtu.be/BWAWq7n6PCk
Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele
quer mostrar mais alguns termos. O programa encerrará quando ele disser que
quer mostrar 0 termos."""

print('=' * 30)
print('Gerador de PA')
print('=' * 30)
p = int(input('\nPrimeiro termo: '))
r = int(input('Razão: '))
i = 1
total = 10
mais = 1
while mais != 0:
    while i <= total:
        print(p, end=', ')
        p += r
        i += 1
    print('PAUSA')
    mais = int(input('Mais algum termo? '))
    total = mais + total
print('\nProgressão finalizada com {} termos mostrados.'.format(total))
print('FIM!')
0