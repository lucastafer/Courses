# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Informe seu sexo [M/F]:')).strip().upper()[0] # Tira os espaçoes, joga pra maiúsculo e pega só a primeira letra.
while sexo not in 'MF':
        sexo = str(input('Dado inválido. Por favor, informe seu sexo [M/F]:')).strip().upper()[0] # Tira os espaçoes, joga pra maiúsculo e pega só a primeira letra.
print(f'Sexo {sexo} registrado com sucesso.')
