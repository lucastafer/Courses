# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

from time import sleep

print('Diga-me três medidas e eu lhe informo se é possível ou não construir um triângulo com elas.')
a = float(input('Primeira medida: '))
b = float(input('Segunda medida: '))
c = float(input('Terceira medida: '))
print('Processando dados...')
sleep(2)
if a < b + c and b < a + c and c < a + b:
    print('Com as medidas {}, {} e {} é possível formar um triângulo.'.format(a, b, c))
else:
    print('Com as medidas {}, {} e {} não é possível formar um triângulo.'.format(a, b, c))
