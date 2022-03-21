# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética. 
# d) Em que posição está o time da Chapecoense.

tabela = ('Atlético-MG', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Bragantino', 'Corinthians', 'Internacional',
          'Fluminense', 'Cuiabá', 'Athletico-PR', 'Atlético-GO', 'São Paulo', 'Ceará', 'Santos', 'Bahia',
          'Juventude', 'Grêmio', 'América-MG', 'Sport', 'Chapecoense')

print('=' * 31)
print('{:^31}'.format('Brasileirão Série A 2021'))
print('=' * 31)

print('*' * 31)
print(' Lista de times do Brasileirão')
print('*' * 31)
print(tabela)

print('*' * 31)
print('{:^31}'.format('G6 - Seis Primeiros Colocados'))
print('*' * 31)
print(tabela[0:6])

print('*' * 31)
print('{:^31}'.format('Z4 - Zona de Rebaixamento'))
print('*' * 31)
print(tabela[16:20])

print('*' * 31)
print('{:^31}'.format('Clubes em Ordem Alfabética'))
print('*' * 31)
print(sorted(tabela))

print('*' * 31)
print('{:^31}'.format('Em qual posição está meu time ?'))
print('*' * 31)
while True:
    try:
        time = int(input('Escolha o time que deseja saber a colocação:\n[0] América-MG\n[1] Athletico-PR\n[2] Atlético-GO\n[3] Atlético-MG\n[4] Bahia\n[5] Bragantino\n[6] Ceará\n[7] Chapecoense\n[8] Corinthians\n[9] Cuiabá\n[10] Flamengo\n[11] Fluminense\n[12] Fortaleza\n[13] Grêmio\n[14] Internacional\n[15] Juventude\n[16] Palmeiras\n[17] Santos\n[18] Sport\n[19] São Paulo'))
        if not time in range(1, 21):
            raise ValueError
    except ValueError as e:
        print('Código inválido. Escolha um código referente a algum desses times.')
    else:
        break
time2 = sorted(tabela)[time]
print(f'O {time2} está na {(tabela.index(time2)+1)}ª colocação.')
