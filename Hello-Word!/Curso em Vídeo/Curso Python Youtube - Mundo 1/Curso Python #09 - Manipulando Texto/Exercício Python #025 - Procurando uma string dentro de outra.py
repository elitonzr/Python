# https://www.youtube.com/watch?v=WHWGz2Dy1ZU&index=35&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6
# 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Qual seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
