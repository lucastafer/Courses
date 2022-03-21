# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

list = []
r = 'S'
while r == 'S':
    while True:
        try:
            n = int(input('Digite um número:'))
            if not n >= 0:
                raise ValueError
        except ValueError as e:
            print('Por favor digite apenas números inteiros.')
        else:
            break
    list.append(n)
    r = str(input('Quer continuar ? [S/N]')).upper().strip()[0]
    while r not in 'SN':
        r = str(input('Opção inválida. Por favor, escolha S para Sim e N para Não.\nQuer continuar ? [S/N]')).upper().strip()[0]

print(f'Foram digitados {len(list)} valores.')
list.sort(reverse=True)
print(f'Valores digitados, em ordem decrescente: {list}')
if 5 in list:
    print(f'O valor 5 apareceu na {list.count(5)} vez(es) na lista.')
else:
    print('O valor 5 não apareceu na lista.')
