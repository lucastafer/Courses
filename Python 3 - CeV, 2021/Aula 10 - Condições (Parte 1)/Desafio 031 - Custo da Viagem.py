# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

dist = int(input('Qual a distância da viagem que quer realizar ?'))
if dist <= 200:
    print('O preço da passagem para uma viagem de {:.2f} Km é de R${:.2f}.'.format(dist, 0.50 * dist))
else:
    print('O preço da passagem para uma viagem de {:.2f} Km é de R${:.2f}.'.format(dist, 0.45 * dist))

# Em Condição Simplificada

dist = int(input('Qual a distância da viagem que quer realizar ?'))
preço = dist * 0.50 if dist <= 200 else dist * 0.45
print('O preço da passagem para sua viagem de {:.2f} Km será R${:.2f}.'.format(dist, preço))
