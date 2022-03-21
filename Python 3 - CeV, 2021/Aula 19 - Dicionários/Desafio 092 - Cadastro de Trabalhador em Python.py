# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
# Obs: aposenta = 35 anos de contribuição

dict = {}

dict['NOME:'] = str(input('NOME: ')).title()
dict['ANO DE NASCIMENTO:'] = int(input('ANO DE NASCIMENTO: '))
dict['Nº CTPS:'] = int(input('CTPS (DIGITE 0 SE NÃO POSSUIR): '))
if dict['Nº CTPS:'] != 0:
    dict['ANO DE CONTRATAÇÃO:'] = int(input('ANO DE CONTRATAÇÃO: '))
    dict['SALÁRIO:'] = float(input('SALÁRIO:'))
    dict['APOSENTADORIA:'] = dict['ANO DE CONTRATAÇÃO:'] - dict['ANO DE NASCIMENTO:'] + 35
for k, v in dict.items():
    print(f'{k} {v}')
