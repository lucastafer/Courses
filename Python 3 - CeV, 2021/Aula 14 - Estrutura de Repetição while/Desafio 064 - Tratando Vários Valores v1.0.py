# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

soma = numeros = n = 0
while n != 999:
    n = int(input('Digite um número inteiro:'))
    if n != 999:
        numeros += 1
    if n != 999:
        soma += n
print(f'Foram inseridos {numeros} números e a soma entre eles é {soma}.')
