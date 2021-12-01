"""https://youtu.be/iHjsUxNA-wo
Exercício Python 048: Faça um programa que calcule a soma entre todos os
números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
"""

soma = 0
count = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        count += 1
print('A soma dos {} números ímpares múltiplos de três de 1 até 500 é: {}'.format(count, soma))
