n = int(input('Digite um número: '))

# Modo 1
# d = n * 2
# t = n * 3
# r = n ** (1/2)

# print('O dobro de {} é: {}.'.format(n, d))
# print('O tripo de {} é: {}.'.format(n, t))
# print('A raiz quadrada de {} é: {:.2f}.'.format(n, r))

# Modo 2
print('\nO dobro de {} vale {}.'.format(n, (n * 2)))
print('O tripo de {} vale {}.'.format(n, (n * 3)))
print('A raiz quadrada de {} vale {:.2f}.'.format(n, (pow(n, (1/2)))))
