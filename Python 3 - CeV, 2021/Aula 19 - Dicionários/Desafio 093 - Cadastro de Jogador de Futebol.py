# Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. 
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

dict = {}
gols = 0
dict['NOME DO JOGADOR:'] = str(input('NOME DO JOGADOR:')).title()
dict['PARTIDAS JOGADAS:'] = int(input('PARTIDAS JOGADAS:'))
for c in range(0, dict['PARTIDAS JOGADAS:']):
    dict[f'GOLS FEITOS NA {c+1}ª PARTIDA:'] = int(input(f'GOLS FEITOS NA {c+1}ª PARTIDA:'))
    gols += dict[f'GOLS FEITOS NA {c+1}ª PARTIDA:']
print()
print('======= ESTATÍSTICAS ======= ')
print()
for k, v in dict.items():
    print(f'{k} {v}')
print(f'TOTAL DE GOLS NO CAMPEONATO: {gols}')
print(f'MÉDIA DE GOLS POR PARTIDA: {gols/dict["PARTIDAS JOGADAS:"]}')


# Opção Guanabara
jogador = {}
partidas = []
jogador['nome'] = str(input('Nome do Jogador:'))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou ?'))
for w in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {w}')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for x, y in jogador.items():
    print(f'O campo {x} tem o valor {y}')
print('-=' * 30)
print(f' O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for z, y in enumerate(jogador["gols"]):
    print(f' => Na partida {z}, fez {y} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
