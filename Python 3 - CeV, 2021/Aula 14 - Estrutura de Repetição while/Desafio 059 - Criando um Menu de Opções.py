# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

print('='*20)
print('   CALCULADORA.PY')
print('='*20)
x = float(input('Informe um valor:'))
y = float(input('Informe outro valor:'))
opcao = int(input('[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair do programa\n Qual sua opção ?'))
if opcao == 1:
    print(f'A soma entre {x} e {y} é {x+y}.')
elif opcao == 2:
    print(f'A multiplicação entre {x} e {y} é igual a {x*y}.')
elif opcao == 3 and x > y:
    print(f'Entre os números {x} e {y}, o maior entre eles é o {x}.')
elif opcao == 3 and x < y:
    print(f'Entre os números {x} e {y}, o maior entre eles é o {y}.')
elif opcao == 3 and x == y:
    print(f'Os números {x} e {y} são iguais, portanto não há maior entre eles.')
while opcao != 5:
    opcao = int(input('[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair do programa\n Qual sua opção ?'))
    if opcao == 1:
        print(f'A soma entre {x} e {y} é {x + y}.')
    elif opcao == 2:
        print(f'A multiplicação entre {x} e {y} é igual a {x * y}.')
    elif opcao == 3 and x > y:
        print(f'Entre os números {x} e {y}, o maior entre eles é o {x}.')
    elif opcao == 3 and x < y:
        print(f'Entre os números {x} e {y}, o maior entre eles é o {y}.')
    elif opcao == 3 and x == y:
        print(f'Os números {x} e {y} são iguais, portanto não há maior entre eles.')
    if opcao == 4:
        x = float(input('Informe um valor:'))
        y = float(input('Informe outro valor:'))
        opcao = int(input('[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair do programa\n Qual sua opção ?'))
        if opcao == 1:
            print(f'A soma entre {x} e {y} é {x + y}.')
        elif opcao == 2:
            print(f'A multiplicação entre {x} e {y} é igual a {x * y}.')
        elif opcao == 3 and x > y:
            print(f'Entre os números {x} e {y}, o maior entre eles é o {x}.')
        elif opcao == 3 and x < y:
            print(f'Entre os números {x} e {y}, o maior entre eles é o {y}.')
        elif opcao == 3 and x == y:
            print(f'Os números {x} e {y} são iguais, portanto não há maior entre eles.')
print('Finalizando...')
sleep(1.5)
print('Fim do programa, volte sempre!')
