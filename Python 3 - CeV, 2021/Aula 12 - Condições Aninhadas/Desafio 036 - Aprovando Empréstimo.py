# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

from time import sleep
print('-=-'*12)
print(' SIMULADOR DE EMPRÉSTIMO TAFERBANK')
print('-=-'*12)

NOME = input('Olá, visitante! Qual seu nome ?').title()
IMOVEL = float(input(f'Muito bem, {NOME}. Digite o valor do imóvel que deseja adquirir.'))
SALARIO = float(input('Certo, então o imóvel que deseja custa R${:.2f}. Agora digite a sua renda mensal.'.format(IMOVEL)))
PERIODO = int(input('Muito bem, então sua renda mensal é de R${:.2f}. Por fim, em quantos anos pretende quitar seu financiamento ?'.format(SALARIO)))
MESES = PERIODO * 12
PARCELA = IMOVEL/MESES
print('Processando dados, por favor aguarde...')
sleep(3)
if PARCELA <= SALARIO * 0.30:
    print(f'Muito bem, {NOME}! Seu empréstimo foi aprovado.')
    print('O valor de cada prestação será R${:.2f}.'.format(PARCELA))
elif PARCELA >= SALARIO * 0.30:
    print(f'{NOME}, infelizmente seu empréstimo foi negado.')
    print('Motivo da recusa: valor da parcela superior a 30% de sua renda mensal.')
    print('Valor de cada Parcela: R${:.2f}.\n Valor de 30% da renda mensal: R${:.2f}.'.format(PARCELA, SALARIO * 0.30))
