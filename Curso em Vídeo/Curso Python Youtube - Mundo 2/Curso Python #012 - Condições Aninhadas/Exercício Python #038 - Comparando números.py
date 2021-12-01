"""https://www.youtube.com/watch?v=iuPbB9uHczM&t=2s
Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais"""


n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O primeiro valor é maior {}, que o segundo {}.'.format(n1, n2))
elif n2 > n1:
    print('O segundo valor é maior {}, que o primeiro {}.'.format(n2, n1))
else:
    print('Não existe valor maior, os dois são iguais {} = {}.'.format(n2, n1))
