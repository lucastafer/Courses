# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
from time import sleep

x = int(input('Tente adivinhar o número de 0 a 5 que estou pensando. Digite um número:'))
numero = random.randrange(5)
if  numero == x:
    print('Muito bem, você acertou!')
else:
    print('Pééém! Errado! O número que pensei foi {}.'.format(numero))
    
# Ou

print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar!')
print('-=-' * 20)
y = int(input('Pensei! Chute um número:'))
print('Processando...')
sleep(2)
computador = random.randint(0, 5)
if computador == y:
    print('Muito bem, você acertou!')
else:
    print('Pééém! Errado! O número que pensei foi {}.'.format(computador))
