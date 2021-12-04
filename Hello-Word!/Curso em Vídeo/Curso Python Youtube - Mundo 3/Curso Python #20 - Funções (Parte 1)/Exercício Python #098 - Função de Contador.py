"""https://youtu.be/DCBlt_z2UOE
Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que
receba três parâmetros: início, fim e passo. Seu programa tem que realizar três
contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada"""

from time import sleep

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    print('-='*20)
    print(f'Contando de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end=' ', flush=True)
            cont += passo
            sleep(0.5)
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end=' ', flush=True)
            cont -= passo
            sleep(0.5)
    print('FIM!')
    print('-=' * 20)


contador(1, 10, 1)
contador(10, 0, 2)
print(f'{"Personalizado":^40}')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = abs(int(input('Passo: ')))
contador(i, f, p)
