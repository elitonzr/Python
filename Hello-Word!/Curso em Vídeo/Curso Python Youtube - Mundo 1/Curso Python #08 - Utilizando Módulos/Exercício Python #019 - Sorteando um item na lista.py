# Exercício Python 019:
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import randrange, choice

primeiro = str(input('Primeiro aluno: '))
segundo = str(input('Segundo aluno: '))
terceiro = str(input('Terceiro aluno: '))
quarto = str(input('Quarto aluno: '))

# primeiro = 'Paulo'
# segundo = 'Ana'
# terceiro = 'Pedro'
# quarto = 'Maria'

lista = [primeiro, segundo, terceiro, quarto]
escolhido = choice(lista)
print('\nO aluno escolhido foi {}.'.format(escolhido))

# escolhido = randrange(1, 4)
# print('\nO aluno escolhido foi {}.'.format(lista[escolhido]))

