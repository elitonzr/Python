"""https://youtu.be/1u7oA8ckjAc
Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""

t = (int(input('Digite um número: ')),
    int(input('Digite um número: ')),
     int(input('Digite um número: ')),
     int(input('Digite um número: ')))
print(f'Você digitou os valores {t}')
print(f'O valor 9 apareceu {t.count(9)} Vezes')
if 3 in t:
    print(f'O valor 3 apareceu na {t.index(3) +1}° posição')
else:
    print('O valor 3 não foi digitando nenhuma vez')
print('Os valores pares digitados foram: ', end='')
for c in t:
    if c != 0:
        if c % 2 == 0:
            print(c, end=' ')