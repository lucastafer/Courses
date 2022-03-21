# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('LUFFY', 'PYTHON', 'RENGOKU', 'KANYE', 'SHANKS',
            'DONDA', 'JAVASCRIPT', 'HISOKA','CHOPPER', 'ZORO')

for c in palavras:
    print(f'\nNa palavra {c} temos as vogais ', end='')
    for letra in c: # Para cada letra de c, verificar se tem 'AEIOU' nelas e printar a que tiver.
        if letra.upper() in 'AEIOU':
            print(letra, end=' ')

# O primeiro for analisa cada elemento da tupla.
# O segundo for analisa cada letra dentro da tupla.
