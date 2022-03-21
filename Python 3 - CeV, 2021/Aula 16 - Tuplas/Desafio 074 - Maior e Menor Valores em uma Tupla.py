# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

import random

valores = tuple(random.sample(range(1, 100), 5))
print(f'Valores gerados: {valores}')
print(f'Maior valor gerado: {max(valores)}')
print(f'Menor valor gerado: {min(valores)}')
