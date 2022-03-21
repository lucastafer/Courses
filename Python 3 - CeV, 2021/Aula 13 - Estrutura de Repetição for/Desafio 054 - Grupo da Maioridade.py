# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

atual = 2021
totmaior = 0
totmenor = 0
for c in range(1, 8):
    ano = int(input(f'Em que ano a {c}ª pessoa nasceu ?'))
    if ano > 2021:
        print('Isso não é possível, vou desconsiderar esse.')
    else:
        print(f'Essa pessoa tem {atual-ano} anos.')
    if ano <= 2003:
        print('Portanto, essa pessoa é maior de idade.')
        totmaior += 1
    elif ano > 2003:
        print('Portanto, essa pessoa é menor de idade.')
        totmenor += 1
print(f'Dessas sete pessoas, {totmaior} são maiores de idade.')
print(f'Dessas sete pessoas, {totmenor} são menores de idade.')


# Opção com o módulo datetime
from datetime import date
hoje = date.today().year
totalmaior = 0
totalmenor = 0

for pess in range (1, 8):
    nasc = int(input(f'Em que ano a {pess}ª pessoa nasceu ?'))
    idade = hoje - nasc
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print(f'Ao todo tivemos {totalmaior} pessoas maiores de idade.')
print(f'Ao todo tivemos {totalmenor} pessoas menores de idade.')
