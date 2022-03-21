# Exemplos iniciais:
print('\033[1:30:44mOlá, mundo!') # Assim ficou a linha inteira colorida.
print('\033[1:30:44mOlá, mundo!\033[m') # O \033[m delimita até onde a cor vai, pois é como se colocasse "sem cor" a partir dele.

# Delimitando as cores:
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[34m{}\033[m.'.format(a, b)) # Não precisa escolher a cor dos três (atyle, text and bg), pode ser só de um ou dois.
print('Os valores são \033[35:40m{}\033[m e \033[36:40m{}\033[m.'.format(a, b))
print('Os valores são \033[7:31m{}\033[m e \033[7:32m{}\033[m.'.format(a, b))

# Colocando as cores por .format:
nome = input('Qual seu nome ?')
print('Prazer em te conhecer, {}{}{}!'.format('\033[4:35m', nome, '\033[m'))

# Fazendo uma linha de códigos para as cores que for usar no programa:
name = input('What"s your name ?:')
colors = {'clean':'\033[m',
          'blue':'\033[34m',
          'yellow':'\033[33m',
         'blackandwhite':'\033[7:30m'}
print('Nice to meet you, {}{}{}!'.format(colors['blue'], name, colors['clean']))
