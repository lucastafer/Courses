# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

print('~' * 26)
print('  Sequência de Fibonacci')
print('~' * 26)

n = int(input('Quantos termos você quer mostrar ?')) # Número de termos que o usuário deseja ver.
ultimo = 0
penultimo = 1
print('{} → {} →'.format(ultimo, penultimo), end='')
cont = 3
while cont <= n:
    proximo = ultimo + penultimo             # Para descobrir o proximo número, somamos o penúltimo + o último.
    print(' {} →'.format(proximo), end='')   # Printamos então o próximo...
    ultimo = penultimo                       # Agora, para o programa considerar os "novos" ultimos e penultimos para
    penultimo = proximo                      # calcular os próximos termos, precisamos por que o termo que era o último,
    cont += 1                                # agora corresponde ao penúltimo, e que o que era o proximo agora é o penultimo.
print(' Fim!')
