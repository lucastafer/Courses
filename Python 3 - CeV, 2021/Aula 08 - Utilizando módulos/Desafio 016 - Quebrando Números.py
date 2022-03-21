# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math

x = float(input('Digite um número qualquer, de preferência todo fodido.'))
inteiro = math.trunc(x)
print('A porção inteira de {} é igual a {}.'.format(x, inteiro))
