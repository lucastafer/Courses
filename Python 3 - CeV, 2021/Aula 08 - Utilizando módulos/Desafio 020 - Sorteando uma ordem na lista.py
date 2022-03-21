# O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

A1 = str(input('Insira o nome do primeiro aluno.'))
A2 = str(input('Insira o nome do segundo aluno.'))
A3 = str(input('Insira o nome do terceiro aluno.'))
A4 = str(input('Insira o nome do quarto aluno.'))
lista=[A1, A2, A3, A4]
shuffle(lista)
print('A ordem das apresentações será {}.'.format(lista))
