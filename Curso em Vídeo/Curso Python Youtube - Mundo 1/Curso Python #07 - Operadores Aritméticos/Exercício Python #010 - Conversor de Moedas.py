# https://youtu.be/xM4AX3Lp2mo
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere US$1,00 = R$3,27.

d = float(input('Quanto dinheiro você tem na carteira? R$'))
print('Com R${} você pode comprar US${:.2f}'.format(d, (d/3.27)))
