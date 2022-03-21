# Melhore o Desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

print('-=' * 10)
print('   Gerador de PA')
print('-=' * 10)
primeiro = int(input('Informe o primeiro termo da PA:'))
razão = int(input('Informe a razão da PA:'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais   # O total vai ser o total + mais (começará com 10)
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += razão   # Os novos termos serão somados à razão da PA
        cont += 1
    print('PAUSA.')
    mais = int(input('Quantos termos você quer mostrar a mais ?'))
print(f'Progressão finalizada com {total} termos mostrados.')
