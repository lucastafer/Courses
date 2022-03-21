# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

x = float(input('Digite um ângulo.'))
rad = math.radians(x)
sen = math.sin(rad)
cos = math.cos(rad)
tg = math.tan(rad)
print('Muito bem! O Seno desse ângulo é {:.2f}, o Cosseno é {:.2f} e a Tangente é {:.2f}.'.format(sen, cos, tg))
