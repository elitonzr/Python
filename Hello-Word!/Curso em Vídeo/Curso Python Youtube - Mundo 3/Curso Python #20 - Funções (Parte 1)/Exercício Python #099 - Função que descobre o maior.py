"""https://youtu.be/vp9UX7wr92o
Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que
receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os
valores e dizer qual deles é o maior."""

from time import sleep


def maior(* num):
    cont = nmaior = 0
    print('-=' * 20)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.5)
        if cont == 0 or nmaior < valor:
            nmaior = valor
        cont += 1
    print(f'Foram informados {cont} valores no total.')
    print(f'O maior valor informado foi: {nmaior}')


maior(2, 9, 4, 5, 7, 1)
maior(2, 4, 7, 0)
maior(1, 2)
maior(6)
maior()
