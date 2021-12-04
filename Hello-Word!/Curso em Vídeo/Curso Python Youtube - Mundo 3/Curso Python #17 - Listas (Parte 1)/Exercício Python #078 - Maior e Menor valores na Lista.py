"""https://youtu.be/q8Z1cRdJnfk
Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi
o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
print(f'\nVocê digitou {lista}')
print(f'Maior valor digitado foi {max(lista)} na posição ', end='')
for i in range(0, 5):
    if lista[i] == max(lista):
        print(f' {i}...', end='')
print(f'\nMenor valor digitado foi {min(lista)} na posição ', end='')
for i in range(0, 5):
    if lista[i] == min(lista):
        print(f' {i}...', end='')
