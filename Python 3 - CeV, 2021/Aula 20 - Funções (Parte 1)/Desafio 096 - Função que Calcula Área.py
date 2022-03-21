# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def linha(txt):
    print('~'*(len(txt)))
    print(txt)
    print('~' * (len(txt)))


linha(f'{"Calculadora de Área":^}')


comprimento = float(input('Comprimento do terreno (m²): '))
largura = float(input('Largura do terreno (m²): '))


def area(comprimento, largura):
    a = comprimento * largura
    print(f'Um terreno com {comprimento} m de comprimento e {largura} m de largura tem uma área total de {a} m².')


area(comprimento, largura)


# Opção Guanabara

def área(l, c):
    a = l * c
    print(f'Um terreno {c} m x {largura} m tem uma área de {a} m².')


print('Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l,c)
