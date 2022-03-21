# Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
# Ao final, mostre o conteúdo das três listas geradas.

todos = []
impar = []
par = []
r = 'S'
while r == 'S':
    n = int(input('Digite um número: '))
    todos.append(n)
    if n % 2 == 0:
        par.append(n)
    if n % 2 != 0:
        impar.append(n)
    r = str(input('Quer continuar ? [S/N]')).upper().strip()[0]
    while r not in 'SN':
        r = str(input('Opção inválida. Insira S para Sim e N para Não.\nQuer continuar ? [S/N]')).upper().strip()[0]
print(f'Valores digitados: {todos}')
print(f'Valores pares digitados: {par}')
print(f'Valores ímpares digitados: {impar}')
