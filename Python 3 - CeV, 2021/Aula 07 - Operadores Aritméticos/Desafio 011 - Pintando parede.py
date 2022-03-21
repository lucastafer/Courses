# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

h = float(input('Qual é a altura dessa parede ?'))
w = float(input('E qual é a largura dessa parede ?'))
a = h * w
tn = (h * w) / 2
print('Considerando então que a parede tenha {} metros de altura por {} metros de largura, logo sua área é de {} m².'.format(h, w, a))
print('Sendo assim, já que 1 litro de tinta pinta 2m², para pintar toda essa parede serão necessários {} litros de tinta.'.format(tn))
