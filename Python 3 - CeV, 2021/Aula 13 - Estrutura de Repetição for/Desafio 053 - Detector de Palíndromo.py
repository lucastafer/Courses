# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

print('+'*27)
print('  DETECTOR DE PALÍNDROMOS')
print('+'*27)

x = str(input('Digite uma frase ou palavra:')).upper().replace(' ', '').replace('-', '')
y = str(x[::-1]).replace(' ', '').replace('-', '')
print(x, y)
if x == y:
    print(f'O contrário de {x} é {y}.')
    print(f'{x} é palíndromo.')
else:
    print(f'O contrário de {x} é {y}.')
    print(f'{x} não é palíndromo.')


# Opção com .join
print('+'*27)
print('  DETECTOR DE PALÍNDROMOS')
print('+'*27)
frase = str(input('Digite uma frase ou uma palavra:')).strip().upper() # Li a frase, jogando tudo para maiusculo
palavras = frase.split() # Splitei a frase, para gerar uma lista
junto = ''.join(palavras) # Juntei tudo numa única str
inverso = ''
for letra in range(len(junto) - 1,  -1, -1): # Fizemos um inverso dela, para ver se é ou não palíndromo.
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo.')
else:
    print('Não temos um palíndromo.')
