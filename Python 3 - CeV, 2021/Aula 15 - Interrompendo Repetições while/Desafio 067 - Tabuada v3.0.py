# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo.

while True:
    n = int(input('Digite um número que queira saber a tabuada:'))
    if n < 0:# Colocar sempre logo após o input, porque aí nem aparece "a tabuada é..."
        break
    print(f'A tabuada de {n} é:')
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n * c}')
print('PROGRAMA DE TABUADA ENCERRADO.\nVOLTE SEMPRE!')
