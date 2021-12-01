"""https://youtu.be/rJaBLOW57Jg
Exercício Python 050: Desenvolva um programa que leia seis números inteiros e
mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""

soma = 0
count = 0

for c in range(1, 7):
    n = int(input(' Digite o {}° número: '.format(c)))
    if n % 2 == 0:
        soma += n
        count += 1
print('A soma dos {} números pares é: {}'.format(count, soma))
