# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

x = float(input('Insira aqui o salário atual do colaborador.'))
y = float(input('Insira aqui o percentual de aumento que deseja conferir ao salário desse funcionário.'))
z = x * (y/100+1)
print('Com o aumento de {y}%, o novo salário desse colaborador será de R${:.2f}.'.format(z))
