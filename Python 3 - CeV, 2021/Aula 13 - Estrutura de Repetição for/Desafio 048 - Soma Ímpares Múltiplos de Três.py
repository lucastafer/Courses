# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0: #if c for divisível por 3
        soma = soma + c # Para receber o que ela tem + os numeros que se enquadrarem naquele coiso.
print(f'A soma entre todos os números ímpares múltiplos de 3 no intervalo entre 1 e 500 é de {soma}.')

# Adicionando um contador, para mostrar quantos numeros impares multiplos de 3 ele achou.
soma2 = 0
cont = 0
for c2 in range(1, 501, 2):
    if c2 % 3 == 0:
        soma2 = soma2 + c2
        cont = cont + 1 # Cuidado com a indentação, pois se ele não estiver na mesma linha da soma, ele contará todos os 250 números ímpares.
print(f'A soma de todos os {cont} valores ímpares múltiplos de 3 no intervalo de 1 a 500 é igual a {soma2}.')

# Opção simplificada
soma3 = 0
cont3 = 0
for c3 in range(1, 501, 2):
    if c3 % 3 == 0:
        soma3 += c
        cont3 += 1
print(f'A soma de todos os {cont3} valores ímpares múltiplos de 3 no intervalo de 1 a 500 é igual a {soma3}.')
