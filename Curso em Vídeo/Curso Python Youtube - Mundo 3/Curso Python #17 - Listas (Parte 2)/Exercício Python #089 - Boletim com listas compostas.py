"""https://youtu.be/7xrCJnniqMw
Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e
guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de
cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente."""

#lista = [['Maria', 8.5, 6.5], ['Claudio', 3.5, 2], ['Ana', 10, 10], ['Roberto', 4.75, 8.45], ['Paulo', 3.5, 7.15]]
lista = []
cadastro = []
aluno = 0
while True:
    cadastro.append(str(input('Nome: ')).upper().strip())
    cadastro.append(float(input('Nota 1: ')))
    cadastro.append(float(input('Nota 2: ')))
    lista.append(cadastro[:])
    cadastro.clear()
    res = ' '
    while res not in "SN":
        res = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if res in 'N':
        break
print(f'{"N°":<5} {"NOME":<10} {"MÉDIA":^5}')
print('-'*25)
for pos in range(0, len(lista)):
    media = (lista[pos][1] + lista[pos][2]) / 2
    print(f'{pos:<5} ', end='')
    print(f'{lista[pos][0]:<10} ', end='')
    print(f'{media:<5.1f} ')
print('-'*25)
while aluno != 999:
    aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if aluno == 999:
        break
    print(f'As notas de {lista[aluno][0]} foram {lista[aluno][1]} e {lista[aluno][2]}')
    print('-' * 25)
