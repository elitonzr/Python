from random import randint
from time import sleep


def sorteia():
    lista = []
    print('-=' * 20)
    print('Analisando os valores passados...')
    v = randint(1, 10)
    for i in range(0, v):
        sleep(0.5)
        n = randint(0, 10)
        lista.append(n)
        print(f'{lista[i]} ', end='', flush=True)
    print(f'Foram informados {len(lista)} valores no total.')
    maior = 0
    for c in lista:
        if c > maior or maior == 0:
            maior = c
    print(f'O maior valor informado foi: {maior}')


rept = randint(1, 10)
cont = 0
print(f'seram realizados {rept} sorteios')
while cont <= rept:
    print(f'Sorteio {cont}')
    sorteia()
    cont += 1
