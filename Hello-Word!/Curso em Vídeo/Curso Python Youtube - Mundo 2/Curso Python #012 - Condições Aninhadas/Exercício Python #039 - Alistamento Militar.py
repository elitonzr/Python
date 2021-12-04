"""https://www.youtube.com/watch?v=ePwP4gU_waY
Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""

from datetime import date

atual = date.today().year
a = int(input('Ano de nascimento? '))
i = atual - a
print('Quem nasceu em {} tem {} anos em {}.'.format(a, i, atual))
if i > 18:
    print('Você já deveria ter se alistato há {} anos.'.format(i - 18))
    print('Seu alistamento foi em {}.'.format(a + 18))
elif i < 18:
    print('Faltam {} anos para o seu alistamento.'.format(18 - i))
    print('Seu alistamento séra em {}.'.format(a + 18))
else:
    print('Você tem que se alistar IMEDIATAMENTE!')
