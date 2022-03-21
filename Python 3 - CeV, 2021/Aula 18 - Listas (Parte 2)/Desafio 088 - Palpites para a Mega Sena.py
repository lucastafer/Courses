# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import sample
from time import sleep

print('-'*37)
print('{:^37}'.format('GERADOR DE NÚMEROS PARA MEGA SENA'))
print('-'*37)
jogos = []

qtd_de_jogos = int(input('Quantas combinações de 6 números você deseja ?'))
for c in range(0, qtd_de_jogos):
    n = sorted(sample(range(1, 61), 6))
    jogos.append(n[:])
    print(f'Jogo {c + 1}: {n}')
    sleep(0.75)
print()
print('Boa sorte!')
