# https://www.youtube.com/watch?v=EQQt-6QqXOs&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=32
# 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.
nome = (str(input('Digite seu nome completo: ')).strip())
# nome = 'Eliton Roberto Monteiro'
print('Analisando seu nome...')
maiuscula = nome.upper()
print('Seu nome em maiúsculas é {}'.format(maiuscula))
minuscula =nome.lower()
print('Seu nome em minúsculas é {}.'.format(minuscula))
semespaço = nome.strip()
totalletras = len(semespaço) - nome.count(' ')
print('Seu nome tem ao todo {} letras.'.format(totalletras))
lista = nome.split()
primeironome = lista[0]
print('Seu primeiro nome é {} e ele tem {} letras.'.format(primeironome, len(primeironome)))
