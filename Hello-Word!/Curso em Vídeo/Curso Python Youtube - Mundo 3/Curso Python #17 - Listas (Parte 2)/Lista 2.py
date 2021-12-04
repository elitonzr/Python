pessoa = []
listapesro = ['Pedro', 25]
listamaria = ['Maria', 19]
listajoao = ['João', 32]
pessoa.append(listapesro)
pessoa.append(listamaria)
pessoa.append(listajoao)
print(pessoa)
print(pessoa[0][0])
print(pessoa[1][1])
print(pessoa[2][0])
print(pessoa[1])

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

galera2 = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for c in galera2:
    print(f'{c[0]} tem {c[1]} anos de idade.')

galera3 = []
dado = []
for i in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(str(input('Idade: ')))
    galera3.append(dado[:])
    dado.clear()
print(galera3)

for p in galera3:
    if p[1] >= 21: