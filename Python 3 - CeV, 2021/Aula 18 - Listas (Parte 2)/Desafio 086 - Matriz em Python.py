# Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

matrizL1 = []
matrizL2 = []
matrizL3 = []
matriz = []
for c in range(0, 3):
    n = int(input(f'Digite um valor para [0, {c}]:'))
    matrizL1.append(n)
    matriz.append(matrizL1[:])
    matrizL1.clear()
for c in range(0, 3):
    n = int(input(f'Digite um valor para [1, {c}]:'))
    matrizL2.append(n)
    matriz.append(matrizL2[:])
    matrizL2.clear()
for c in range(0, 3):
    n = int(input(f'Digite um valor para [2, {c}]:'))
    matrizL3.append(n)
    matriz.append(matrizL3[:])
    matrizL3.clear()
print(f'{str(matriz[0]):^5} {str(matriz[1]):^5} {str(matriz[2]):^5}')  #Tem que por o str antes do (matriz) pra ele aceitar assim
print(f'{str(matriz[3]):^5} {str(matriz[4]):^5} {str(matriz[5]):^5}')
print(f'{str(matriz[6]):^5} {str(matriz[7]):^5} {str(matriz[8]):^5}')


# Opção do Guanabara (professor)

mat = [0, 0, 0], [0, 0, 0], [0, 0, 0]  # Declarando que dentro de cada linha ele terá três valores, não precisa usar append. Depois vai substituir esses zeros por valores.
                                       
# Um laço dentro do outro pra alimentar todos aqueles campos com 0.
for l in range(0, 3): # For de linha
    for c in range(0, 3): #For de Coluna
        mat[l][c] = int(input(f'Digite um valor para [{l}, {c}]:')) #Matriz na linha [l] e coluna na linha [c].
for l in range(0, 3): # Esses for são para mostrar a estrutura na tela, o de cima era pra alimentar os campos.
    for c in range(0, 3):
        print(f'[{mat[l][c]:^5}]', end='')
    print() # Quebra linha
