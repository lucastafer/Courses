# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. 
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep

dict = {}
for c in range(1, 5):
    Nome = input("Nome do Jogador:").title()
    Valor = randint(1, 6)
    dict[Nome] = Valor
print('>>>>> BOA SORTE A TODOS! <<<<<')
for k, v in dict.items():
    print(f'{k} tirou {v} nos dados!')
    sleep(1)
ordem_decrescente = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse=True)}
print('>>>>> RANKING FINAL <<<<<')
cont = 0
for k, v in ordem_decrescente.items():
    print(f'{cont + 1}ª Lugar: {k}, que tirou {v}!')
    cont += 1
    
    
# Opção Guanabara

from operator import itemgetter

jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}
ranking = list()
print('Valores Sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado...')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) # Se o IG for 0 coloca em ordem de Chave, e 1 de valor
print('-=' * 30)                                                # ou seja, do maior pro menor devido ao reverse True.
print(' == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1}º Lugar: {v[0]} com {v[1]}.')
print(f'Parabéns ao vencedor {ranking[0][0]}!')
