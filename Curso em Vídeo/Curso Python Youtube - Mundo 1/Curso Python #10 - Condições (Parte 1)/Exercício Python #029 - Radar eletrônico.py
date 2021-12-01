"""https://www.youtube.com/watch?v=hgJ_ETNGSj8&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=40
Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite."""

v = int(input("Qual a velocidade atual do carro?: "))
if v > 80:
    print("\nMULTADO! você exedeu o limite permitido de 80Km/h.")
    m = (v - 80) * 7
    print("Você deve pagar uma multa de R${:.2f}!.".format(m))
else:
    print("\nTenha um bom dia! Dirija com segurança!")
