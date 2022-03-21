# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

from math import factorial

r = 'S'
while r == 'S':
    n = int(input('Digite um número inteiro:'))
    print(f'O fatorial de {n} é igual a {factorial(n)}.')
    r = str(input('Deseja continuar [S/N] ?')).upper()
print('Fim do programa, volte sempre!')
