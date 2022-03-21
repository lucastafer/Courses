# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

from time import sleep

print('-=-' * 10)
print('   ESCOLA CURSO EM VÍDEO')
print('-=-' * 10)

ficha = []
situaçao = ''

while True:
    nome = str(input('Nome:')).title()
    while True:
        try:
            P1 = float(input('Nota P1:'))
            while P1 > 10 or P1 < 0:
                raise ValueError
        except ValueError as e:
            print('Valor inválido. Por favor, apenas números de 0 a 10.')
        else:
            break
    while True:
        try:
            P2 = float(input('Nota P2:'))
            while P2 > 10 or P2 < 0:
                raise ValueError
        except ValueError as e:
            print('Valor inválido. Por favor, apenas números de 0 a 10.')
        else:
            break
    media = (P1 + P2) / 2
    if media >= 5:
        situaçao = 'Aprovado'
    else:
        situaçao = 'Reprovado'
    ficha.append([nome, [P1, P2], media])
    stop = str(input('Quer continuar ?\n[S] Sim\n[N] Não')).upper().strip()[0]
    while stop not in 'NS':
        stop = str(input('Opção inválida. Digite S para Sim e N para Não.\nQuer continuar ?\n[S] Sim\n[N] Não')).upper().strip()[0]
    if stop == 'N':
        break
    print('-=-' * 10)
print('-=-' * 10)
print()
print('-' * 40)
print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}{"Situação":>15}')
print('-' * 40)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}{situaçao:>15}')
    print('-' * 40)
while True:
    especifico = int(input('Digite o Nº do aluno para ver sua notas detalhadamente.\n999 para encerrar.'))
    if especifico == 999:
        print('Finalizando...')
        sleep(1)
        break
    if especifico < len(ficha):
        print(f'Notas de {ficha[especifico][0]}: {ficha[especifico][1]}')
print('Programa encerrado com sucesso.')
