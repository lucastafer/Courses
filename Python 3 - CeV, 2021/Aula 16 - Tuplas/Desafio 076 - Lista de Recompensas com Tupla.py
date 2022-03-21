# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

print('=' * 35)
print('{:^35}'.format('ONE PIECE BOUNTIES'))
print('=' * 35)
lista = ('Monkey D. Luffy', 1500000000.00, 'Vinsmoke Sanji', 330000000.00, 'Roronoa Zoro', 320000000.00,
              'Shanks', 4048900000.00, 'Trafalgar Law', 500000000.00)
for c in range (0, len(lista)): # Um range de 0 até o comprimento da lista (len).
    if c % 2 == 0: # Usamos par ou ímpar para separar as escritas dos valores.
        print(f'{lista[c]:.<21}', end='')
    else:        # pra retornar o valor ímpar/par c da lista
        print(f'฿{lista[c]:>13.2f}') # Como a escrita foi admitida como par, os valores serão o else (ímpares).
print('=' * 35)
