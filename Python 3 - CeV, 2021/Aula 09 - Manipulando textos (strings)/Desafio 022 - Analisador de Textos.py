# Crie um programa que leia o nome completo de uma pessoa e mostre: 
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = str(input('Olá, meu nome é Professor Oak. Qual seu nome?'))
print('Certo, seu nome então é', nome.upper(),'!')
print('Ou, caso preferir,', nome.lower(),'!')
caract = nome.split()
print('No total, seu nome possui {} caractéres.'.format(len(''.join(caract))))
print('No total, seu primeiro nome possui {} letras.'.format(len(caract[0])))
