"""https://youtu.be/Hd7Ycaj61xE
Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar
palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta."""

from random import randint

jogo = []
print('-'*30)
print(F'{"GERADOR DE JOGOS DA MEGA SENA":^30}')
print('-'*30)
nj = int(input('Quantos jogos deseja gerar? '))
for j in range(0, nj):
    for n in range(0, 6):
        if len(jogo) == 0:
            jogo.append(randint(0, 60))
        else:
            while True:
                nm = randint(0, 60)
                if nm not in jogo:
                    jogo.append(nm)
                    break
    jogo.sort()
    print(f'Jogo {j + 1:>3}: {jogo}')
    jogo.clear()
