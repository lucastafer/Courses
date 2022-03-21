# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). 
# No final, mostre a lista ordenada na tela.

lista = []
for c in range(0, 5):
    n = int(input(f'Digite o {c+1}º valor: '))
    if c == 0 or n > lista[-1]:  # Se ele for o primeiro ou se ele for maior que o último valor.
        lista.append(n)
        print('Adicionado ao final da lista.')
    else: # Para descobrir em qual posição adicionar os próximos n, tem que verificar todo o vetor.
        pos = 0 # Posições
        while pos < len(lista):         # Enquanto a posição for menor que o len de lista, ele vai verificando
            if n <= lista[pos]:         # Vou verificar dentro de cada posição se o número que quero inserir (n) é menor ou
                lista.insert(pos, n)    # igual a ele. Se ele for menor ou igual, insiro em uma posição específica.
                print(f'Adicionado à posição {pos}.')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {lista}')
