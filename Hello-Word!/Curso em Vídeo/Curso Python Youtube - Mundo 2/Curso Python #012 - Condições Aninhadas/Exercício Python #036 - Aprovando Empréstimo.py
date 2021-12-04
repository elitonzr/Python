"""https://www.youtube.com/watch?v=IV13X0QOMU8&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=3
Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o
valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do
salário ou então o empréstimo será negado."""

v = float(input('Qual é o valor da casa? R$'))
s = float(input('Qual é o seu salário? R$'))
a = float(input('Quantos anos você vai pagar? '))
p = v / (a * 12)
if p > s * 0.3:
    print('Empréstimo NEGADO! A prestação R${:.2f} é superior a 30% do seu salário.'.format(p))
else:
    print('Empréstimo APROVADO! A prentação séra de R${:.2f}.'.format(p))
