# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matrizL1 = []
matrizL2 = []
matrizL3 = []
matriz = []
terceiracoluna = []
segundalinha = []
somapares = 0

for c in range(0, 3):
    n = int(input(f'Digite um valor para [0, {c}]:'))
    if c == 2:
        terceiracoluna.append(n)
    matrizL1.append(n)
    matriz.append(matrizL1[:])
    matrizL1.clear()
for c in range(0, 3):
    n = int(input(f'Digite um valor para [1, {c}]:'))
    if c == 2:
        terceiracoluna.append(n)
    segundalinha.append(n)
    matrizL2.append(n)
    matriz.append(matrizL2[:])
    matrizL2.clear()
for c in range(0, 3):
    n = int(input(f'Digite um valor para [2, {c}]:'))
    if c == 2:
        terceiracoluna.append(n)
    matrizL3.append(n)
    matriz.append(matrizL3[:])
    matrizL3.clear()
for p in matriz:
    if p[0] % 2 == 0:
        somapares += p[0]
print('Sua matriz ficou assim:')
print(f'{str(matriz[0]):^5} {str(matriz[1]):^5} {str(matriz[2]):^5}')
print(f'{str(matriz[3]):^5} {str(matriz[4]):^5} {str(matriz[5]):^5}')
print(f'{str(matriz[6]):^5} {str(matriz[7]):^5} {str(matriz[8]):^5}')
print(f'A soma de todos os valores pares digitados é {somapares}.')
print(f'A soma dos valores da terceira coluna é igual a {sum(terceiracoluna)}.')
print(f'O maior entre os valores da segunda linha é o {max(segundalinha)}.')
