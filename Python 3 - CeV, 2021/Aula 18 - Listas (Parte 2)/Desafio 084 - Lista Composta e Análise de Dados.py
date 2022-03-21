# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

temp = []     # Lista Temporária
princ = []    # Lista principal
peso = []     # Lista com os pesos

while True:
    temp.append(str(input('NOME:'.title())))
    temp.append(float(input('PESO:')))
    princ.append(temp[:])
    peso.append(temp[1])
    temp.clear()
    stop = str(input('Quer continuar ? [S/N]')).upper().strip()[0]
    while stop not in 'SN':
        stop = str(input('Opção inválida. Escolha S para Sim e N para não.\nQuer continuar ? [S/N]')).upper().strip()[0]
    if stop == 'N':
        break
print(f'Ao todo foram cadastradas {len(princ)} pessoas.')
print(f'O maior peso foi de {max(peso):.2f}Kg, sendo este o peso de ', end='')
for p in princ:
    if p[1] == max(peso):
        print(f'{p[0]} ', end='')
print(f'\nO menor peso foi de {min(peso):.2f}Kg, sendo este o peso de ', end='')
for p in princ:
    if p[1] == min(peso):
        print(f'{p[0]} ', end='')
