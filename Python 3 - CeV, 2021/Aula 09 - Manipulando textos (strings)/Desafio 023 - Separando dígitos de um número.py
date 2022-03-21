# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = int(input('Digite um número.'))
n = str(numero)
print('Certo, então você escolheu {}. Analisando esse número, temos:'.format(numero))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))
# Esse método dá pau para números com menos de 4 dígitos.

# Opção com Método Matemático, resolvendo o problema acima:
x = int(input('Digite um número.'))
print('Certo, então você escolheu {}. Analisando esse número, temos:'.format(x))
u = x // 1 % 10
d = x // 10 % 10
c = x // 100 % 10
m = x // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
