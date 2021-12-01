"""https://youtu.be/QhS829x6up4
Exercício Python 087: Aprimore o desafio anterior,
mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""

matriz = [[[0], [0], [0]], [[0], [0], [0]], [[0], [0], [0]]]
soma_pares = 0
soma_terceira_coluna = 0
maior_valor_segunda_linha = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para{linha, coluna}: '))
print('-=-'*10)
for linha in range(0, len(matriz)):
    for coluna in range(0, len(matriz)):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
        if coluna == 2:
            soma_terceira_coluna += matriz[linha][2]
        if linha == 1:
            if coluna == 0 or matriz[1][coluna] > maior_valor_segunda_linha:
                maior_valor_segunda_linha = matriz[1][coluna]
    print()
print('-=-'*10)
print(f'A soma dos valores pares é: {soma_pares}')
print(f'A soma dos valores da terceira coluna é: {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é: {maior_valor_segunda_linha}')
