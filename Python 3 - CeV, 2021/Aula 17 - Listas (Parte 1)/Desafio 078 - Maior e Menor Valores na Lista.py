# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = []

for v in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {v}:')))
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)}, presente nas posições', end='')
for v, z in enumerate(valores):
    if z == max(valores):
        print(f' ➾ {v} ➾', end='')
print('FIM!')
print(f'\nO menor valor digitado foi {min(valores)}, presente nas posições', end='')
for v, z in enumerate(valores):
    if z == min(valores):
        print(f' ➾ {v} ➾', end='')
print(' FIM!')
