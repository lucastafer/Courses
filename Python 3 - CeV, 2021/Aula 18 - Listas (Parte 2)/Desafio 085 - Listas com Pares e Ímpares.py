# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
# No final, mostre os valores pares e ímpares em ordem crescente.

temporaria = []
principal = []
print('---------------------------')
print('Escolha 7 números inteiros')
print('---------------------------')
for c in range(0, 7):
    temporaria.append(int(input(f'Digite o {c+1}º número:')))
    principal.append(temporaria[:])
    temporaria.clear()
principal.sort()
print('Números pares digitados:',end='')
for v in principal:
    if v[0] % 2 == 0:
        print(f'{v[0]}', end=' ➾ ')
print('Fim!')
print('\nNúmeros ímpares digitados: ',end='')
for v in principal:
    if v[0] % 2 != 0:
        print(f'{v[0]}', end=' ➾ ')
print('Fim!')


# Opção com lista única

num = [], []
for x in range(0, 7):
    valor = int(input(f'Digite o {x + 1}º número:'))
    if valor % 2 == 0:
        num[0].append(valor)
    if valor % 2 != 0:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'Números pares cadastrados: {num[0]}')
print(f'Números ímpares cadastrados: {num[1]}')
