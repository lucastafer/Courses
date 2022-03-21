# Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

n = totalnumeros = 0
valores = list()
r = 'S'
while r == 'S':
    n = valores.append(int(input('Digite um número inteiro:')))
    r = str(input('Quer continuar [S/N] ?')).upper().strip()[0]
    totalnumeros += 1
print(f'Foram lidos {totalnumeros} números, sendo a média entre eles {sum(valores)/totalnumeros}, o maior valor lido {max(valores)} e o menor valor lido {min(valores)}.')
