"""https://www.youtube.com/watch?v=I-SH3QchuZ4
Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço
normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros"""

v = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque: 10% de desconto')
print('[ 2 ] à vista no cartão: 5% de desconto')
print('[ 3 ] em até 2x no cartão: preço formal')
print('[ 4 ] 3x ou mais no cartão: 20% de juros')
f = int(input('Qual é a opção? '))

if f == 1:
    total = v - v * 0.1
    print('Sua compra vai custar R${:.2f} COM DESCONTO.'.format(total))
elif f == 2:
    total = v - v * 0.05
    print('Sua compra vai custar R${:.2f} COM DESCONTO.'.format(total))
elif f == 3:
    total = v
    print('Sua compra será parcelada em 2x de {} SEM JUROS.'.format(v / 2))
elif f == 4:
    total = v * 0.2 + v
    p = int(input('Quantas parcelas? '))
    print('Sua compra séra parcelada em {}x de R${:.2f} COM JUROS.'.format(p, total / p))
else:
    total = 0
    print('Opção invalida, tete novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(v, total))
