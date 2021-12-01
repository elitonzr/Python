"""https://www.youtube.com/watch?v=ZiC5NgSGJXU
Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER"""

from datetime import date

a = int(input('Ano de nascimento? '))
i = date.today().year - a
print('O atleta tem {} anos.'.format(i))
if i <= 9:
    print('Classificação: MIRIN.')
elif 9 < i <= 14:
    print('Classificação: INFANTIL.')
elif 14 < i <= 19:
    print('Classificação: JÚNIOR.')
elif 19 < i <= 25:
    print('Classificação: SÊNIOR.')
else:
    print('Classificação: MASTER.')
