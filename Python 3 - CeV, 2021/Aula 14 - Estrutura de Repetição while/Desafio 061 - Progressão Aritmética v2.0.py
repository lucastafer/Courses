# Refaça o Desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('-=' * 10)
print('   Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo:'))
razão = int(input('Razão da PA:'))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} → '.format(termo), end='')
    termo += razão
    cont += 1
print('Fim!')


# Opção em que pode escolher quantos termos quer ver
print('+' * 22)
print(' 10 TERMOS DE UMA PA')
print('+' * 22)

PT = float(input('Primeiro termo: '))
R = float(input('Razão:'))
NT = float(input('Número de termos: '))
c = 0
print('Sendo o primeiro termo da PA {:.0f} e a razão {:.0f}, os {:.0f} termos dessa PA são:'.format(PT, R, NT))
while c != NT:
    n = PT + (c * R)
    c += 1
    print('{:.0f}'.format(n), end=' → ')
print('FIM!')
