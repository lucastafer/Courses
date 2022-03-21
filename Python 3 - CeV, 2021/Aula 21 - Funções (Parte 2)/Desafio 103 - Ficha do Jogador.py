# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. 
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.


def ficha(nome=0, gols=0):
    print('-' * 30)
    nome = str(input('Nome do Jogador:')).title().strip()
    if nome == '':
        nome = '<desconhecido>'
    try:
        gols = int(input('Gols marcados:'))
        if gols < 0:
            raise ValueError
    except ValueError as e:
        gols = 0
    if gols == 0:
        return f'O jogador {nome} não marcou nenhum gol no campeonato.'
    if gols == 1:
        return f'O jogador {nome} marcou {gols} gol no campeonato.'
    if gols > 1:
        return f'O jogador {nome} marcou {gols} gols no campeonato.'


print(ficha())
