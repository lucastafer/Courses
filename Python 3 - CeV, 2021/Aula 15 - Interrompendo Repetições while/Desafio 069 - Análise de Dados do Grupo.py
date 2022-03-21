# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

print('-' * 19)
print('  FICHA CADASTRAL')
print('-' * 19)
contmaior = homem = mulher = 0
while True:
    while True:
        try:
            idade = int(input('Idade:'))
            if not 0 <= idade <= 100000000000000000000:
                raise ValueError("Opção inválida!")
        except ValueError as e:
            print("Opção inválida. Informe a idade em números.")
        else:
            break
    if idade >= 18:
        contmaior += 1
    sexo = str(input('Sexo [M/F]:')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Opção inválida.\nInforme seu sexo [M/F]:')).upper().strip()[0]
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade >= 20:
            mulher += 1
    stop = str(input('Deseja continuar cadastrando [S/N] ?')).strip().upper()[0]
    while stop not in 'SN':
        stop = str(input('Opção inválida. Tecle S para Sim ou N para Não.\nDeseja continuar cadastrando [S/N] ?')).strip().upper()[0]
    if stop == 'N':
        break
print(f'Total de pessoas com 18 anos ou mais: {contmaior}')
print(f'Total de homens: {homem}')
print(f'Total de mulheres com 20 anos ou mais: {mulher}')
