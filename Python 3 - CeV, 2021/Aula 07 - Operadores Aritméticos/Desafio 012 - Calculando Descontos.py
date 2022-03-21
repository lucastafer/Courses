# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

x = input('Procure por algum produto que tenha interesse.')
P = 210
PD = float(P * 0.95)
print('O preço desse produto é R${:.2f}.'.format(P))
print('Porém, comprando acima de 10 unidades, conseguimos um desconto de 5% e o preço cai para R${:.2f}.'.format(PD))
