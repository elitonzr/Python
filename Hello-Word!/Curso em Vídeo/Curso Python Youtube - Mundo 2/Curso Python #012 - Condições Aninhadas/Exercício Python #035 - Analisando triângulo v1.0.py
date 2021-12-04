"""Para construir um triângulo não podemos utilizar qualquer medida, tem que seguir a condição de existência:
Para construir um triângulo é necessário que a medida de qualquer um dos lados seja menor que a soma das medidas dos outros dois e maior que o valor absoluto da diferença entre essas medidas."""


a = float(input('Primeiro seguimento: '))
b = float(input('Segundo seguimento: '))
c = float(input('Terceiro Seguimento: '))

if a < b + c and a > abs(b - c) and b < a + c and b > abs(a - c) and c < b + a and c > abs(b - a):
	print('Sim, é possível formar um triângulo')
else:
	print('Não, é possível formar um triângulo')