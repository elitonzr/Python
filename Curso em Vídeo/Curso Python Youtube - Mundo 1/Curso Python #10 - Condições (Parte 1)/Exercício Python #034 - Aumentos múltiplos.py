"""https://www.youtube.com/watch?v=Sfadj_AzKHw&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=45
Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%."""


n = float(input('\nQual é o seu salário? R$'))
if n > 1250:
    s = n + (n * 0.1)
else:
    s = n + (n * 0.15)
print('\nQuem ganhava R${:.2f} passa a ganhar R${:.2f}.'.format(n, s))
