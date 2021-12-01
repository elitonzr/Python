"""https://youtu.be/QDpwjBYRcVE
Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela."""

lista = list()
for c in range(0, 5):
    numero = int(input(f'Digite o {c + 1}° número: '))
    if c == 0 or numero > lista[-1]:
        lista.append(numero)
        print('Adicionado ao final da lista.')
    else:
        if numero < min(lista):
            lista.insert(0, numero)
            print('Adicionado ao posição 0 da lista.')
        else:
            pos = 0
            while pos < len(lista):
                if numero <= lista[pos]:
                    lista.insert(pos, numero)
                    print(f'Adicionado na posição {pos} da lista.')
                    break
                pos += 1
print(f'Os Valores digitados em ordem foram: {lista}')