# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

print('-=-'*12)
print(' CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('-=-'*12)
ANO = int(input('DIGITE SEU ANO DE NASCIMENTO:'))
IDADE = 2021 - ANO

if IDADE <= 9:
    print(f'IDADE: {IDADE}\nSUA CATEGORIA É MIRIM.')
elif IDADE > 9 and IDADE <= 14:
    print(f'IDADE: {IDADE}\nSUA CATEGORIA É INFANTIL.')
elif IDADE > 14 and IDADE <= 19:
    print(f'IDADE: {IDADE}\nSUA CATEGORIA É JÚNIOR.')
elif IDADE > 19 and IDADE <= 25:
    print(f'IDADE: {IDADE}\nSUA CATEGORIA É SÊNIOR.')
elif IDADE > 25:
    print(f'IDADE: {IDADE}\n SUA CATEGORIA É MASTER.')

print('-=-'*12)
print(' CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('-=-'*12)
ANO = int(input('DIGITE SEU ANO DE NASCIMENTO:'))
IDADE = 2021 - ANO

# Simplificando as conditions

if IDADE <= 9:
    print(f'IDADE: {IDADE}\nSUA CATEGORIA É MIRIM.')
elif IDADE <= 14:
    print(f'IDADE: {IDADE}\nSUA CATEGORIA É INFANTIL.')
elif IDADE <= 19:
    print(f'IDADE: {IDADE}\nSUA CATEGORIA É JÚNIOR.')
elif IDADE <= 25:
    print(f'IDADE: {IDADE}\nSUA CATEGORIA É SÊNIOR.')
else:
    print(f'IDADE: {IDADE}\n SUA CATEGORIA É MASTER.')
