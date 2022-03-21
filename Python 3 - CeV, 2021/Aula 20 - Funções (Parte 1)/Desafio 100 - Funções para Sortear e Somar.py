# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep

numeros = []
soma = 0


def sorteia(list):
    print('Sorteando 5 números: ', end=' ')
    for c in range(0, 5):
        n = randint(0, 10)
        list.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.5)
    print('Feito!')


def somapar(list):
    soma = 0
    for num in numeros:
        if num % 2 == 0:
            soma += num
    print(f'Soma dos valores pares em {numeros}: {soma}')


sorteia(numeros)
somapar(numeros)
