# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math

co = float(input('Digite o comprimento do Cateto Oposto.'))
ca = float(input('Digite o comprimento do Cateto Adjacente.'))
coca = (co ** 2 + ca**2)
h = math.sqrt(coca)
print('A hipotenusa desse triãngulo é igual a {}.'.format(h))
