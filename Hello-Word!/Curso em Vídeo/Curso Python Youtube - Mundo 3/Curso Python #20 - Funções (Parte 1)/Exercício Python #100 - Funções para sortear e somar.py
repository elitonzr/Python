"""https://youtu.be/MEs-41JcuhM
Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas
funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai
colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os
valores pares sorteados pela função anterior."""
from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores: ', end='')
    for i in range(0, 5):
        lista.append(randint(1, 10))
        print(f'{lista[i]}', end=' ', flush=True)
        sleep(0.5)
    print('PRONTO!')


def somapar(lista):
    soma = 0
    for i in numeros:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = list()
sorteia(numeros)
somapar(numeros)
