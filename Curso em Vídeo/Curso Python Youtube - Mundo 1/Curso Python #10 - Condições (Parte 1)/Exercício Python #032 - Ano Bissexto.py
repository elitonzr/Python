"""https://www.youtube.com/watch?v=cyGY_83m4Xw&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=43
Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto."""


from datetime import date
ano = int(input('\nQue ano quer analisar? Coloque 0 para analisar o ano atual. '))
if ano ==0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\nO ano {} é BISSEXTO.'.format(ano))
else:
    print('\nO ano {} NÂO é BISSEXTO.'.format(ano))
