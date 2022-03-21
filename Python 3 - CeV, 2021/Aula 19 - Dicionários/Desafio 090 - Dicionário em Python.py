# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

boletim = {}
print('====== Boletim ======')
boletim['Nome'] = str(input('Nome: ')).title()
boletim['Média'] = float(input('Média: '))
if boletim['Média'] >= 6:
    boletim['Situação'] = 'Aprovado'
else:
    boletim['Situação'] = 'Recuperação'
print('=' * 21)
for k, v in boletim.items():
    print(f'{k}: {v}')
