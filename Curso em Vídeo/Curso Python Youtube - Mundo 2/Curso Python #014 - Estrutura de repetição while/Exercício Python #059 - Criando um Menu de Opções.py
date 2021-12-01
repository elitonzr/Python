"""https://youtu.be/OBJL5vPj4-E
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""


n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
opcao = 0
while opcao != 5:
    print('''\n    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('\n >>>>> Qual é a sua opção? '))
    if opcao == 1:
        resultado = n1 + n2
        print('\nA soma entre {} + {} é {}.'.format(n1, n2, resultado))
    elif opcao == 2:
        resultado = n1 * n2
        print('\nO resultado de {} x {} é {}.'.format(n1, n2, resultado))
    elif opcao == 3:
        if n1 > n2:
            print('\nEntre {} e {} o maior valor é {}.'.format(n1, n2, n1))
        elif n1 < n2:
            print('\nEntre {} e {} o maior valor é {}.'.format(n2, n1, n2))
        else:
            print('\n{} e {} são iguais.'.format(n1, n2))
    elif opcao == 4:
        print('\nInforme os números novamente:')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif opcao == 5:
        print('\nFinalizando...')
    else:
        print('\nOpção inválida. Tente novamente')
print('Fim do Programa!')