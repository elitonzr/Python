# Nessa aula, vamos aprender operações com String no Python.
# As principais operações que vamos aprender são o Fatiamento de String,
# Análise com len(), count(), find(),
# transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().

frase = 'Curso em vídeo Python'
# C u r s o   e m   V í  d  e  o      P y  t  h  o  n
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

# Retorna do 0 a 4 (Curso).
print(frase[:5])

# Retorna do frase pulando de duas em duas letras..
print(frase[::2])

# Retorna do 6 a 7 (em).
print(frase[6:8])

# Retorna do 9 a 13 (Vídeo).
print(frase[9:14])

# Retorna do 15 até o fim (Python).
print(frase[15:])

# Retorna a quantidade de caracter (21).
print(len(frase))

# Retorna a quantidade de caracter 'o' na frase (3).
print(frase.count('o'))

# Retorna o primeiro local onde o 'o' foi encontrado (4).
print(frase.find('o'))

# Retorna -1 quando não é encontrado a palavra.
print(frase.find('android'))

# Retorna (false) quando não é encontrado a palavra.
print('curso' in frase)

# Retorna a frase inteira em maiúscula.
print(frase.upper())

# Retorna a frase inteira em minuscula.
print(frase.lower())

# Retorna a primeira letra da frase em maiúscula.
print(frase.capitalize())

# Retorna a primeira letra de todas as palavras da frase em maiúscula.
print(frase.title())

# Retorna a a frase substituindo 'python' por 'Android'.
print(frase.replace('Python', 'Android'))

# atribui outra frase para a variavel frase.
frase = '   Aprenda Python  '

# Retorna o valor de frase.
print(frase)

# Retorna a frase sem os espaços.
print(frase.strip())

# Retorna a frase sem os espaços a direita.
print(frase.rstrip())

# Retorna a frase sem os espaços a esquerda.
print(frase.lstrip())

# atribui outra frase para a variavel frase.
frase = 'Curso em vídeo Python'

# Retorna uma lista da frase, separa a frase nos espaços.
print(frase.split())

# atribui outra frase para a variavel frase.
frase = 'Curso em vídeo Python'

# Retorna a lista separada por '-'.
print('-'.join(frase))

# Retorna um texto.
print('''\n"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore 
et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut 
aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum 
dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui 
officia deserunt mollit anim id est laborum."''')