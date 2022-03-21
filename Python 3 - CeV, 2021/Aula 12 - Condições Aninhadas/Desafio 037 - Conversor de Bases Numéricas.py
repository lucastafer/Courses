# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

# Opção sem fatiamento de str, fica esses 2 digitos antes do número indicando o que ele é.
numero = int(input('DIGITE UM NÚMERO INTEIRO:'))
base = int(input('DIGITE UMA DAS BASES DE CONVERSÃO::\n[1] BINÁRIO\n[2] OCTAL\n[3] HEXADECIMAL'))
if base == 1:
    print(f'O NÚMERO {numero} PARA BINÁRIO FICA: {bin(numero)}.')
elif base == 2:
    print(f'O NÚMERO {numero} PARA OCTAL FICA: {oct(numero)}.')
elif base == 3:
    print(f'O NÚMERO {numero} PARA HEXADECIMAL FICA: {hex(numero)}.')
else:
    print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE.')

# Para retirar esses dois dígitos antes do número, utilizar fatiamento de str.

numero2 = int(input('DIGITE UM NÚMERO INTEIRO:'))
base2 = int(input('ESCOLHA UMA DAS BASES PARA CONVERSÃO:\n[1] BINÁRIO\n[2] OCTAL\n[3] HEXADECIMAL'))
if base2 == 1:
    print(f'{numero2} EM BINÁRIO FICA: {oct(numero2)[2:]}.')
elif base2 == 2:
    print(f'{numero2} EM OCTAL FICA: {oct(numero2)[2:]}')
elif base2 == 3:
    print(f'{numero2} EM HEXADECIMAL FICA: {hex(numero2)[2:]}')
else:
    print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE.')
