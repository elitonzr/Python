"""https://youtu.be/8BgSqrOpKvU
Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você
deve mostrar, para cada palavra, quais são as suas vogais."""

texto = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS',
         'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for palavra in texto:
    print(f'\nNa palavra {palavra} temos', end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')
