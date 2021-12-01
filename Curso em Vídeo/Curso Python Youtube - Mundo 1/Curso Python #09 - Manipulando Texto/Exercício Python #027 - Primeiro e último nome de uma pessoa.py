# #027: Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

n = str(input('Digite seu nome completo: ')).strip().split()
print('Seu primeiro nome é {}.'.format(n[0]))
print('Seu último nome é {}.'.format(n[len(n) - 1]))
