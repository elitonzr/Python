"""https://youtu.be/-QkOIHJ1Chw
Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai
"pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar
até acertar, mostrando no final quantos palpites foram necessários para vencer."""

from random import randint
n = randint(0, 10)
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qaul foi?')
p = 0
palpite = 0
while p != n:
    p = int(input('Qual é seu palpite? '))
    palpite += 1
    if p > n:
        print('Menos... Tente mais uma vez.')
    else:
        print('Mais... Tente mais uma vez.')
print('\nParabéns! Você acertou após {} tentativas'.format(palpite))
