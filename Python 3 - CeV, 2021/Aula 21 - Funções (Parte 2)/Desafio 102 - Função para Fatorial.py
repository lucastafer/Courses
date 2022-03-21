# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

from math import factorial


def fatorial(num=1, show=0):
    """
    Função que calcula o fatorial de algum número.
    :param num: número cujo fatorial será calculado.
    :param show: Se show receber S (Sim), o processo de cálculo será mostrado.
    Se show receber N(Não), só o resultado será exibido.
    :return: O valor fatorial de um número n.
    """
    f = factorial(num)
    if show == 'S':
        for c in range(num, 0, -1):
            if c > 1:
                print(f'{c} x ', end='')
            elif c == 1:
                print(f'{c} = ', end='')
        print(factorial(num))
    elif show == 'N':
        print(f'Cálculo não solicitado, resultado do fatorial de {num}: {factorial(num)}.')
    return f


num = int(input('Digite o número que deseja ver seu fatorial:'))
show = str(input('Deseja ver o cálculo completo desse fatorial ?\n[S] Sim\n[N] Não')).strip().upper()[0]
fatorial(num, show)
help(fatorial)
