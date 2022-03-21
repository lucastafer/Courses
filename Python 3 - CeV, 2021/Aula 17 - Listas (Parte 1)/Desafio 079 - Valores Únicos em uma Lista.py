# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. 
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

r = 'S'
num = []
while r == 'S':
    while True:
        try:
            x = int(input('Digite um número:'))
            if not x >= 0:
                raise ValueError
        except ValueError as e:
            print('Valor inválido. Por favor, apenas números inteiros.')
        else:
            break
    if x in num:
        print('Esse você já digitou, não vou considera-lo novamente.')
    else:
        print('Valor adicionado com sucesso!')
        num.append(x)
    r = str(input('Quer continuar ? [S/N]')).upper().strip()[0]
    while r not in 'SN':
        r = str(input('Opção inválida. Por favor, escolha S para Sim e N para Não.\nQuer continuar ? [S/N]')).upper().strip()[0]
num.sort()
print(f'Você digitou os valores {num}')
