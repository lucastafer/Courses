# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

x = float(input('Digite um valor de temperatura em graus ºC.'))
y = x * 1.8 + 32
print('{} ºC em Fahrenheit fica {}ºF.'.format(x, y))
