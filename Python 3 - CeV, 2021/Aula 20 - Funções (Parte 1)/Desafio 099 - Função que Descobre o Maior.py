#  Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
#  Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*val):
    print('------------------------------------')
    print('Analisando os valores informados...')
    print('------------------------------------')
    if len(val) == 0:
        print('Nenhum valor foi informado.')
    elif len(val) > 0:
        print(val, end=' ')
        print(f'→ Foram informados {len(val)} valores. ')
        print(f'O maior valor informado foi {max(val)}.')
    print('------------------------------------')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
