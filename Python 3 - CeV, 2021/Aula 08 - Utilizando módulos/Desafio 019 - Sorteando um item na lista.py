# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

a = str(input('Insira aqui o nome do aluno 1.'))
b = str(input('Insira aqui o nome do aluno 2.'))
c = str(input('Insira aqui o nome do aluno 3.'))
d = str(input('Insira aqui o nome do aluno 4.'))
x = random.choices([a, b, c, d])
print('O aluno sorteado para apagar a lousa é o {}.'.format(x))

# Ou

A1 = str(input('Insira aqui o nome do primeiro aluno.'))
A2 = str(input('Insira aqui o nome do segundo aluno.'))
A3 = str(input('Insira aqui o nome do terceiro aluno.'))
A4 = str(input('Insira aqui o nome do quarto aluno.'))
lista=[A1, A2, A3, A4]
escolhido = random.choice(lista)
print('O aluno sorteado foi {}.'.format(escolhido))
