# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

valores = tuple(int(input('Digite um valor: ')) for c in range(1, 5))
print(f'Você digitou os valores {valores}')
if 9 in valores:
    print(f'O valor 9 apareceu {valores.count(9)} vezes.')
else:
    print('O valor 9 não foi digitado nenhuma vez.')
if 3 in valores:
    print(f'O valor 3 apareceu pela primeira vez na posição {valores.index(3)}.')
else:
    print('O valor 3 não apareceu na relação.')
totpar = 0
print('Valor/valores pares digitados: ', end='')
for n in valores:
    if n % 2 == 0:
        print(n, end=' → ')
        totpar += 1
print('FIM')
if totpar == 0:
    print('Não foi digitado nenhum valor par.')
