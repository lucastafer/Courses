# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. 
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

# Obs: Se quiser que quando o passo receba negaitvo ele corte o sinal tbm, é so fazer o passo receber passo * -1 no inicio.

from time import sleep


def contador(inicio, fim, passo):
    print(f'Iniciando contagem de {inicio} a {fim} de {passo} em {passo}!')
    print('-' * 65)
    if inicio < fim and passo > 0:
        for valor in range(inicio, fim + 1, passo):
            print(f' {valor} ', end=' ➜ ')
            sleep(0.5)
        print('FIM!')
    elif inicio > fim and passo > 0:
        for valor in range(inicio, fim - 1, (passo * -1)):
            print(f'{valor} ', end=' ➜ ')
            sleep(0.5)
        print('FIM!')
    elif inicio < fim and passo == 0:
        passo = 1
        print('Não é possível dar 0 passos! Logo, vou considerar de um em um:')
        for valor in range(inicio, fim + 1, passo):
            print(f' {valor} ', end=' ➜ ')
            sleep(0.5)
        print('FIM!')
    elif inicio > fim and passo == 0:
        print('Não é possível dar 0 passos! Logo, vou considerar de um em um:')
        passo = 1
        for valor in range(inicio, fim - 1, (passo * -1)):
            print(f'{valor} ', end=' ➜ ')
            sleep(0.5)
        print('FIM!')
    elif inicio < fim and passo < 0:
        for valor in range(inicio, fim - 1, (passo * -1)):
            print(f' {valor} ', end=' ➜ ')
            sleep(0.5)
        print('FIM!')
    elif inicio > fim and passo < 0:
        for valor in range(inicio, fim + 1, (passo * -1)):
            print(f'{valor} ', end=' ➜ ')
            sleep(0.5)
        print('FIM!')
    elif inicio == fim:
        print(f'inicio', end='')
        print('FIM!')
    print('-' * 65)


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez! Insira o início, o final e o passo que deseja.')
inicio = int(input('Digite o início: '))
fim = int(input('Digite o fim: '))
passo = int(input('Digite o passo: '))
contador(inicio, fim, passo)
print('>>> PROGRAMA ENCERRADO. VOLTE SEMPRE! <<<')
