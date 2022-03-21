# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

d = int(input('Por quantos dias você ficou com o carro ?'))
km = float(input('Quantos Km você rodou?'))
gd = d * 60
gkm = float(km*0.15)
ct = gd + gkm
print('Considerando o gasto de R$ 60.00 por dia alugado, que lhe custou R${:.2f}, e mais o adicional de \n R$ 0.15 por Km rodado, que ficou em R${:.2f}, logo seu gasto total ficou em R${:.2f}.'.format(gd, gkm, ct))
