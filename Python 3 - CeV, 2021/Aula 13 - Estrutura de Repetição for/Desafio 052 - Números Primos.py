# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número:'))
tot = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[32m', end=' ') # Pintado em verde os números que n é divisível.
        tot += 1
    else:
        print('\033[31m', end=' ') # Pintado em vermelho os números que n não é divisível.
    print('{}'.format(c), end=' ')
print(f'\033[0m\nO número {n} foi divisível {tot} vezes.') # Agora, como sabemos que primo só divide duas vezes, fazer um if:
if tot == 2:
    print('Logo, ele é um número primo.')
else:
    print('Logo, ele não é um número primo, pois um número primo divide-se somente por 1 e por ele mesmo.')
