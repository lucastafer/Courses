# Crie um programa que leia o nome e o preço de vários produtos. O programa
# deverá perguntar seo usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

print('-' * 30)
print('   ARMAZÉM GIUSEPPE CADURA')
print('-' * 30)
soma = maisde1k = maisbarato = cont = 0
prodmaisbarato = ''
while True:
    produto = str(input('PRODUTO:'))
    while True:
        try:
            preço = float(input('VALOR: R$ '))
            if not 0 < preço:
                raise ValueError
        except ValueError as e:
            print("Opção inválida. Informe o valor em números.")
        else:
            break
    if preço > 1000:
        maisde1k += 1
    cont += 1
    soma += preço
    if cont == 1 or preço < maisbarato:
        maisbarato = preço
        prodmaisbarato = produto
    else:
        if preço < maisbarato:
            maisbarato = preço
    stop = str(input('ACRESCENTAR MAIS ITENS ?\n[S] SIM\n[N] NÃO')).strip().upper()[0]
    while stop not in 'SN':
        stop = str(input('OPÇÃO INVÁLIDA. TECLE S PARA SIM OU N PARA NÃO.\nACRESCENTAR MAIS ITENS [S/N] ?')).strip().upper()[0]
    if stop == 'N':
        break
print(f'VALOR TOTAL DA COMPRA: R${soma:.2f}')
print(f'PRODUTOS COM VALOR SUPERIOR A R$ 1.000,00: {maisde1k}')
print(f'PRODUTO MAIS BARATO: {prodmaisbarato}, NO VALOR DE R${maisbarato:.2f}')
