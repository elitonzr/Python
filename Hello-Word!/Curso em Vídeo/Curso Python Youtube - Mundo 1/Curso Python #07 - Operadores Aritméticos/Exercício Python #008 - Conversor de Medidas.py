# https://youtu.be/KjcdG05EAZc
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input('Digite uma distância em metros: '))
print('A medida de {}m corresponde a'.format(m))
print('{}km'.format(m / 1000))
print('{}hm'.format(m / 100))
print('{}dam'.format(m / 10))
print('{}kdm'.format(m * 10))
print('{:.0f}cm'.format(int(m * 100)))
print('{:.0f}mm'.format(int(m * 1000)))
