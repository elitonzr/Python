# https://youtu.be/_QfISzy0IKs
# Desenvolva um programa que leia as duas notas de um aluno.
# Calcule a sua média.

n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
m = (n1 + n2)/2
print('A media entre {} e {} é igual a {:.2f}. '.format(n1, n2, (n1 + n2)/2))
