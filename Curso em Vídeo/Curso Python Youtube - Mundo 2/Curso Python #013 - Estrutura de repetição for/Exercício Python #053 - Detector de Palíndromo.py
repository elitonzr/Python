"""https://youtu.be/5VBWe6BXzRo
Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se
ela é um palíndromo, desconsiderando os espaços.
EX:
 APOS A SOPA
 A SACADA DA CASA
 A TORRE DA DERROTA
 O LOBO AMA O BOLO
 ANOTARAM A DATA DA MARATONA"""

reverse = ''
frase = str(input('Digite uma frase: ').upper().replace(' ', ''))
#reverse = frase[::-1] # Sem usar o for
for c in range(len(frase)-1, -1, -1):
    reverse += frase[c]
print('O inverso de {} é {}.'.format(frase, reverse))
if frase == reverse:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

