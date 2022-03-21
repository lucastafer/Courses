# Crie um programa que simule o funcionamento de um caixa eletrônico. 
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

from time import sleep

print('=' * 30)
print('{:^30}'.format('BANCO PAULA TEJANO'))
print('=' * 30)
saque = int(input('Qual valor você quer sacar ? R$'))
print('Analisando a transação...')
sleep(1)
print('Verificando disponiblidade de cédulas..')
sleep(1)
while True:
    cem = int(saque/100)             # Ele vai testando, caso não seja divisível por cem, vai pro próximo...
    saque = saque % 100              # No final as notas são somadas, totalizando o valor do saque.

    cinquenta = int(saque/50)
    saque = saque % 50

    vinte = int(saque/20)
    saque = saque % 20

    dez = int(saque/10)
    saque = saque % 10

    cinco = int(saque/5)
    saque = saque % 5

    um = int(saque/1)
    saque = saque % 1
    break
print('=========================================')
print(f'Saque autorizado no valor de R${saque}.')
print('=========================================')
print(f'Cédulas de R$ 100,00: {cem}')
print(f'Cédulas de R$ 50,00: {cinquenta}')
print(f'Cédulas de R$ 20,00: {vinte}')
print(f'Cédulas de R$ 10,00: {dez}')
print(f'Cédulas de R$ 5,00: {cinco}')
print(f'Moedas de R$ 1,00: {um}')
