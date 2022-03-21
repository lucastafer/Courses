# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

dict = {}
list = []
mulher = 0
while True:
    dict['NOME:'] = str(input('NOME: ')).title()
    while True:
        try:
            dict['SEXO:'] = str(input('SEXO:\n[M] MASCULINO\n[F] FEMININO ')).upper().strip()[0]
            if dict['SEXO:'] not in 'MF':
                raise ValueError
        except ValueError as e:
            print('OPÇÃO INVÁLIDA. POR FAVOR DIGITE M PARA MASCULINO E F PARA FEMININO.')
        else:
            break
    if dict['SEXO:'] == 'F':
        mulher += 1
    while True:
        try:
            dict['IDADE:'] = int(input('IDADE: '))
            if dict['IDADE:'] < 0:
                raise ValueError
        except ValueError as e:
            print('OPÇÃO INVÁLIDA. POR FAVOR, DIGITE APENAS NÚMEROS.')
        else:
            break
    list.append(dict.copy())
    stop = str(input('DESEJA CONTINUAR ?\n[S] SIM\n[N] NÃO')).upper().strip()[0]
    while stop not in 'SN':
        stop = str(input('OPÇÃO INVÁLIDA. POR FAVOR, DIGITE S PARA SIM E N PARA NÃO.\n[S] SIM\n[N] NÃO')).upper().strip()[0]
    print('==================================')
    if stop == 'N':
        break
print('=========== RESULTADOS ===========')
print('==================================')
print(f'👉 TOTAL DE PESSOAS CADASTRADAS: {len(list)}')
totidades = 0
for c in range(0, len(list)):
    totidades += list[c]['IDADE:']
print(f'👉 MÉDIA DE IDADE: {totidades/len(list):.0f} ')
if mulher == 0:
    print(f'👉 MULHERES CADASTRADAS: N/A')
else:
    print(f'👉 MULHERES CADASTRADAS: ', end='')
    for c in range(0, len(list)):
        if list[c]['SEXO:'] in 'F':
            print(list[c]['NOME:'], end=' ⇔ ')
    print('Fim!')
print(f'👉 INDIVÍDUOS COM IDADE ACIMA DA MÉDIA: ', end='')
for c in range(0, len(list)):
    if list[c]['IDADE:'] > (totidades/len(list)):
        print(list[c]['NOME:'], end=' ⇔ ')
print('Fim!')
print('======== PROGRAMA ENCERRADO ========')
