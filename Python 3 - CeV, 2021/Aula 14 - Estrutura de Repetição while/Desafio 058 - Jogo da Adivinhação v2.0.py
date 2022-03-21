# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random
from time import sleep

print('-=-' * 20)
print('    Vou pensar em um número de 1 a 10. Tente adivinhar!')
print('-=-' * 20)
print('Calma lá, estou pensando...')
sleep(1)
computador = random.randint(1, 10)
jogador = int(input('Pensei!\nChute um número:'))
cont = 1
while computador != jogador:
    jogador = int(input('Errado! Tente novamente...'))
    cont += 1
    if cont == 9 and computador != jogador:
        print(f'Perdeu! Mesmo após 9 tentativas não conseguiu adivinhar.\nEu pensei no número {computador}!')
        break
if cont == 1:
    print(f'Uau, acertou de primeira! Eu pensei mesmo no número {computador}')
elif cont > 1 and cont < 6:
    print(f'Muito bem, você acertou em {cont} tentativas! Não foi de primeira, mas acertou! Eu pensei mesmo no número {computador}.')
elif cont >= 6 and cont < 9:
    print(f'Ufa, suas chances estavam quase acabando, você acertou após {cont} tentativas!\nEu pensei mesmo no número {computador}.')
elif cont == 9 and computador == jogador:
    print(f'Caramba, você acertou na sua última chance! Precisou de {cont} tentativas, eu pensei mesmo no número {computador}.')
    
