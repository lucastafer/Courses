# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

extenso = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE', 'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')
while True:
    try:
        n = int(input('Digite um número inteiro entre 0 e 20:'))
        if n not in range(0, 21):
            raise ValueError
    except ValueError as e:
        print('Número inválido. Digite um número entre 0 e 20.')
    else:
        break
print(f'Você digitou o número {extenso[n]}.')
