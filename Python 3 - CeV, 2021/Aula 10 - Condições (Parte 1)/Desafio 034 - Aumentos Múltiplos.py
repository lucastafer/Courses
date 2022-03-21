# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o salário atual do funcionário.'))

if salario <= 1250:
    print('Para essa quantia incide um aumento de 15 %, logo, o valor passa a ser R$ {:.2f}.'.format(salario * 1.15))
else:
    print('Para essa quantia incide um aumento de 10 %, logo, o valor passa a ser R$ {:.2f}.'.format(salario * 1.10))
