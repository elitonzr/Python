"""https://youtu.be/B3F0IjH5WAM
 Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
 qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal."""


n = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão: ')
print('[1] Converter para BINÁRIO')
print('[2] Converter para OCTAL')
print('[3] Converter para HEXADECIMAL')
o = int(input('Sua opção: '))
if o == 1:
    print('{} convertido para binário é igual a {}'.format(n, bin(n)[2:]))
elif o == 2:
    print('{} convertido para binário é igual a {}'.format(n, oct(n)[2:]))
elif o == 3:
    print('{} convertido para binário é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Opção invalida! Tente novamente')
