""" https://youtu.be/mw1So0r317Y
Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""
jogador = dict()
partidas = list()
time = list()
while True:
    jogador.clear()
    partidas.clear()
    jogador['Nome'] = str(input('Nome do Jogador: ')).capitalize()
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for i in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {i + 1}? ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    resp = ' '
    while True:
        resp = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite somente S ou N.')
    if resp in 'N':
        break
print('-='*30)
print(f'{"cod"} ', end='')
for k in jogador.keys():
    print(f'{k:<15}', end='')
print()
print('--'*30)
for pos, jog in enumerate(time):
    print(f'{pos:<3}', end='')
    for v in jog.values():
        print(f'{str(v):<15}', end='')
    print()
print('--' * 30)
while True:
    resp = int(input('Mostrar dados de qual jogador? (999 para sair) '))
    if resp == 999:
        break
    if resp >= len(time):
        print(f'Jogador não encontrado com o código {resp}')
    else:
        print(f'--LEVANTAMENTO DO JOGADOR {time[resp]["Nome"]}: ')
        for pos, item in enumerate(time[resp]['Gols']):
            print(f'No jogo {pos+1} fez {item} gols.')
        print('--' * 30)
