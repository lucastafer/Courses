# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Digite um número.'))
x = num % 2
if x == 0:
    print('O número indicado {:.0f} é par.'.format(num))
else:
    print('O número indicado {:.0f} é ímpar.'.format(num))
