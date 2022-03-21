# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. 
# Quando o usuário digitar a palavra 'FIM', o programa se  encerrará.

from time import  sleep


def ajuda(com):
    título(f'Acessando o manual do comando {com}...')
    sleep(2)
    help(com)


def título(msg, cor=0):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


comando = ''
while True:
    título('Sistema de Ajuda PyHelp')
    comando = str(input('Função ou Biblioteca >'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('Até logo!')
