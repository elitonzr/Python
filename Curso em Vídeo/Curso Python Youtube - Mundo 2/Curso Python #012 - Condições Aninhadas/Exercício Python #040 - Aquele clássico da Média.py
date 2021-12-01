"""https://www.youtube.com/watch?v=QuWDyUeoaJs
Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no
final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO"""

n1 = float(input('Nota da primeira Prova: '))
n2 = float(input('Nota da segunda Prova: '))
m = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, m))
print('O aluno está ', end='')
if m < 5:
    print('REPROVADO!')
elif 5 <= m <= 6.9:
    print('em RECUPERAÇÃO!')
else:
    print('APROVADO!')
