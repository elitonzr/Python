"""https://youtu.be/84jUX96cs7Q
Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que
indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não
na tela o processo de cálculo do fatorial."""


def fatorial(n, show=False):
    """
    --> Calcula o Fatorial de um número.
    :param n: o número a ser calculado.
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(f' = ', end='')

    return f'{f}'


# Programa Principal
print(fatorial(5, show=True))
help(fatorial)
