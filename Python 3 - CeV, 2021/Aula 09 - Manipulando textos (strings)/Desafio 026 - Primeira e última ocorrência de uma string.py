# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase.')).strip().upper()
print('A letra A aparece na frase {} vezes.'.format(frase.count('A')))
print('A letra A aparece pela primeira vez na posição {}.'.format(frase.find('A')+1))
print('A letra A aparece pela última vez na posição {}.'.format(frase.rfind('A')+1))

# Opção com if e else
frase = str(input('Digite uma frase.')).strip().upper()
x = 'A' in frase
if x == True:
    print('A letra A aparece na frase {} vezes.'.format(frase.count('A')))
    print('A letra A aparece pela primeira vez na posição {}.'.format(frase.find('A') + 1))
    print('A letra A aparece pela última vez na posição {}.'.format(frase.rfind('A') + 1))
else:
    print('A letra A não aparece nenhuma vez nessa frase.')
   
