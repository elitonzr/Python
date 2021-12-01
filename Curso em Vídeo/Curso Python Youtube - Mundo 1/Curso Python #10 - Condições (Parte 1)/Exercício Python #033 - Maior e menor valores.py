"""https://www.youtube.com/watch?v=a_8FbW5oH6I&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=44
Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor."""

a = int(input('Primeiro Valor: '))
b = int(input('Segundo Valor: '))
c = int(input('Terceiro Valor: '))

# Verificando quem é menor.
if a < b and a < c:
    menor = a
elif b < a and b < c:
    menor = b
else:
    menor = c

# Verificando quem é maior.
if a > b and a > c:
    maior = a
elif b > a and b > c:
    maior = b
else:
    maior = c

print('O menor valor digitado foi {}.'.format(menor))
print('O maior valor digitado foi {}.'.format(maior))
