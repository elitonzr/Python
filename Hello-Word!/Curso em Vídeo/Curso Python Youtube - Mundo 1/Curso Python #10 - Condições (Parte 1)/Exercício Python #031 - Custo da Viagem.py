""" https://www.youtube.com/watch?v=PGqHyzWoagc&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=42
Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas."""


n =float(input('\nQual a distância da viagem? '))
if n > 200:
    p = n * 0.45
    print('\nO preço da passagem é de R${:.2f}.'.format(p))
else:
    p = n * 0.5
    print('\nO preço da passagem é de R${:.2f}.'.format(p))
