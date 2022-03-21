# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

print('=' * 75)
print('   Diga-me o peso de 5 pessoas e informarei qual o menor e qual o maior.')
print('=' * 75)
valores = list()
for c in range(1, 6):
    valores.append(float(input(f'Peso da {c}ª pessoa:')))
print('Maior peso: {:.1f} Kg.'.format(max(valores)))
print('Menor peso: {:.1f} Kg.'.format(min(valores)))
