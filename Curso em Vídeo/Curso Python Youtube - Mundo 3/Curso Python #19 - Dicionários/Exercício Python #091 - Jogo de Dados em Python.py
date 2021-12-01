""" https://youtu.be/cwrqIztaAwk
Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham
resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final,
coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""
from random import randint
from time import sleep
from operator import itemgetter
jogo = dict()
for c in range(1, 5):
    jogo[f'Jogador {c}'] = randint(1, 6)
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print(' ===== RANKING DOS JOGADORES =====')
for k, i in enumerate(ranking):
    print(f'    {k+1}° Lugar: {i[0]} com {i[1]}.')
    sleep(1)
