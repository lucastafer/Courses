# Crie um programa que faça o computador jogar Jokenpô com você.

import random
from time import sleep

print('LET S PLAY JO KEN PO!')
NAME = str(input('WHAT S YOUR NAME ?')).upper()
ADV = str(input('UH... I FORGOT THE NAME OF YOUR RIVAL. WHO S HE ?')).upper()
JKP = int(input('OK, LET S GO!\n CHOOSE:\n[1] ROCK\n[2] PAPER\n[3] SCISSOR'))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
sleep(0.5)
PC = random.randint(1, 3)
if PC == 1:
    if JKP == 1:
        print('-=-'*10)
        print(f'{NAME} CHOSE ROCK!')
        print(f'{ADV} CHOSE ROCK!')
        print('-=-' * 10)
        print('DRAW!')
    elif JKP == 2:
        print('-=-' * 10)
        print(f'{NAME} CHOSE PAPER!')
        print(f'{ADV} CHOSE ROCK!')
        print('-=-' * 10)
        print(f'YOU WON! CONGRATULATIONS, {NAME}!')
    elif JKP == 3:
        print('-=-' * 10)
        print(f'{NAME} CHOSE SCISSOR!')
        print(f'{ADV} CHOSE ROCK!')
        print('-=-' * 10)
        print(f'{NOME} LOSE! {ADV} WINS!')
    else:
        print('INVALID PLAY. TRY AGAIN!')
elif PC == 2:
    if JKP == 1:
        print('-=-'*10)
        print(f'{NAME} CHOSE ROCK!')
        print(f'{ADV} CHOSE PAPER!')
        print('-=-' * 10)
        print(f'{NAME} LOSE! {ADV} WINS!')
    elif JKP == 2:
        print('-=-' * 10)
        print(f'{NAME} CHOSE PAPER!')
        print(f'{ADV} CHOSE PAPER!')
        print('-=-' * 10)
        print('DRAW!')
    elif JKP == 3:
        print('-=-' * 10)
        print(f'{NAME} CHOSE SCISSOR!')
        print(f'{ADV} CHOSE PAPER!')
        print('-=-' * 10)
        print(f'YOU WON! CONGRATULATIONS, {NAME}!')
    else:
        print('INVALID PLAY. TRY AGAIN!')
elif PC == 3:
    if JKP == 1:
        print('-=-'*10)
        print(f'{NAME} CHOSE ROCK!')
        print(f'{ADV} CHOSE SCISSOR!')
        print('-=-' * 10)
        print(f'YOU WON! CONGRATULATIONS, {NAME}!')
    elif JKP == 2:
        print('-=-' * 10)
        print(f'{NAME} CHOSE PAPER!')
        print(f'{ADV} CHOSE SCISSOR!')
        print('-=-' * 10)
        print(f'{NAME} LOSE! {ADV} WINS!')
    elif JKP == 3:
        print('-=-' * 10)
        print(f'{NAME} CHOSE SCISSOR!')
        print(f'{ADV} CHOSE SCISSOR!')
        print('-=-' * 10)
        print('DRAW!')
    else:
        print('INVALID PLAY. TRY AGAIN!')
   
