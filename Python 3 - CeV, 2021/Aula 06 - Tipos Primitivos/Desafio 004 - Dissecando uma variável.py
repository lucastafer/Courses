#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

x = str(input('Digite algo.'))
t = (type(x))
print('O tipo primitivo de {} é {}.'.format(x, t))
print('É numérico ?', x.isnumeric())
print('É alfabético ?', x.isalpha())
print('É alfanumérico ?', x.isalnum())
print('Está em maiúsculo?', x.isupper())
print('Está em minúsculo?', x.islower())
print('FIM!')
