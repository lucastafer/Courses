# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

print('PREENCHA OS CAMPOS ABAIXO COM AS INFORMAÇÕES DOS 4 INTEGRANTES DO GRUPO:')
somaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('=' * 20)
    print(f'   {p}º INTEGRANTE')
    print('=' * 20)
    nome = str(input('NOME:')).strip()
    idade = int(input('IDADE:'))
    sexo = str(input('SEXO [M ou F]:'))
    somaidade += idade
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
print('MÉDIA DE IDADE DO GRUPO: {:.0f} ANOS.'.format(somaidade/4))
print('HOMEM MAIS VELHO: {}, {} ANOS.'.format(nomevelho, maioridadehomem).upper())
print(f'MULHERES COM MENOS DE 20 ANOS: {totmulher20}.')
