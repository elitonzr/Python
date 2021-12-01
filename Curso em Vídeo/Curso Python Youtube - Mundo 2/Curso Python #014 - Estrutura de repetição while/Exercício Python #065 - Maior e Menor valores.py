"""https://youtu.be/QNPuPlPM--0
Exercício Python 065: Crie um programa que leia vários números inteiros pelo
teclado. No final da execução, mostre a média entre todos os valores e qual foi
o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele
quer ou não continuar a digitar valores."""

n = 0
media = 0
soma = 0
maior = n
menor = n
i = 0
exit = 'S'
while exit in 'S':
    n = int(input('Digite um número: '))
    soma += n
    i += 1
    if i == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    exit = str(input('Deseja continuar [S/N]: ')).upper().replace(' ', '')[0]
media = soma / i
print('\nVocê digitou {} números e a média foi {:.2f}'.format(i, media))
print('O maior valor foi {}'.format(maior))
print('O menor valor foi {}'.format(menor))
