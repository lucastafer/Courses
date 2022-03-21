# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Informe seu nome completo: ')).strip()
divisao = nome.upper().split()
print('SILVA' in divisao)
