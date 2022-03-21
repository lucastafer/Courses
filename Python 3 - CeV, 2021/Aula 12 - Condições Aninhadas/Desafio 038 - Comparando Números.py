# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
if num1 > num2:
    print(f'{num1} é maior que {num2}, portanto {num1} é o maior valor.')
elif num1 < num2:
    print(f'{num1} é menor que {num2}, portanto {num2} é o maior valor.')
elif num1 == num2:
    print(f'Não há maior valor, pois {num1} e {num2} são iguais.')
