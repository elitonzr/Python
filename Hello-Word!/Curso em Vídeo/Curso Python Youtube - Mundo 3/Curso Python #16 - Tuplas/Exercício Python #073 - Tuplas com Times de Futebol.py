"""https://youtu.be/RexybLcGewA
Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de
Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.
"""
times = ('Corinthians', 'Cruzeiro', 'Palmeiras', 'Santos', 'Grêmio',
         'Flamengo', 'Vasco', 'Chapecoense', 'Atlético-MG', 'Botafogo',
         'Atlético_PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport',
         'Vitória', 'Curitiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('-=' * 15)
print(f'Lista de times do Brasileirão: \033[33m{times}\033[00m')
print('-=' * 15)
print(f'Os 5 primeiros são: \033[33m{times[0:5]}\033[00m')
print('-=' * 15)
print(f'Os 4 últimos são: \033[33m{times[-4:]}\033[00m')
print('-=' * 15)
print(f'Os times em ordem alfabetica: \033[33m{sorted(times)}\033[00m')
print('-=' * 15)
print(f'A chapecoense está na {1 + times.index("Chapecoense")}ª Posição')
print('-=' * 15, '\n')

print('-=' * 15, end='')
print(f'\nLista de times do Brasileirão')
print('-=' * 15)
for c in range(0, len(times)):
    print(f'\033[33m{c + 1:2}ª {times[c]}\033[00m')
print('-=' * 15)
print('')
print('-=' * 15)
print(f'Os 5 primeiros são:')
print('-=' * 15)
for c in range(0, 6):
    print(f'\033[33m{c + 1:2}ª {times[c]}\033[00m')
print('-=' * 15)
print('')
print('-=' * 15)
print(f'Os 4 últimos são:')
print('-=' * 15)
for c in range(len(times) - 1, len(times) - 5, -1):
    print(f'\033[33m{c + 1:2}ª {times[c]}\033[00m')
print('-=' * 15)
print('')
print('-=' * 15)
print(f'Os times em ordem alfabetica:')
print('-=' * 15)
for c in range(0, len(times)):
    print(f'\033[33m{c + 1:2}ª {sorted(times)[c]}\033[00m')
print('-=' * 15)
print('')
print('-=' * 15)
print(f'A chapecoense está na: ', end='')
for c in range(0, len(times)):
    if times[c] == 'Chapecoense':
        print(f'\033[33m{c + 1:2}ª Posição')
print('\033[00m-=' * 15)
