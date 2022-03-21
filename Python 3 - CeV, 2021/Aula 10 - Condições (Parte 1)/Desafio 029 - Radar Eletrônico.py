# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

from time import sleep

velocidade = float(input('VELOCIDADE DO VEÍCULO: '))
limite = int(input('LIMITE DA VIA: '))
multa = (velocidade - limite) * 7
print('PROCESSANDO DADOS...')
sleep(2)
if velocidade > limite:
    print('LIMITE DE VELOCIDADE EXCEDIDO. \nLIMITE: {:.1f} Km/h \nVELOCIDADE: {:.1f} Km/h'.format(limite, velocidade))
    print('APLICAR MULTA NO VALOR DE R$ {:.2f} (R$ 7,00 POR Km/h EXCEDIDO).'.format(multa))
else:
    print('LIMITE DE VELOCIDADE NÃO EXCEDIDO. NÃO SE APLICA MULTA E/OU PENALIDADE.')
