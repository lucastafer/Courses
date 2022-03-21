# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

x = float(input('Quantos reais você tem hoje para trocar por dólares ?'))
d = float(5.22)
rd = x / d
print('Com R${:.2f} você pode trocar hoje por U${:.2f}.'.format(x, rd))

y = float(input('Quantos dólares você quer comprar hoje ?'))
d2 = float(5.22)
dr = y * d2
print('Para comprar U${:.2f} hoje você precisará desembolsar R${:.2f}.'.format(y, dr))

z = float(input('Quantos reais você quer trocar por Euros?'))
e = float(6.15)
re = z / e
print('Com R${:.2f} você pode trocar hoje por €{:.2f}.'.format(z, re))

t = float(input('Quantos Euros você quer comprar hoje ?'))
u = float(6.15)
v = t * u
print('Para comprar €{:.2f} hoje você precisará desembolsar R${:.2f}.'.format(t, v))
