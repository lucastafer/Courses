from time import sleep

print('Diga-me o comprimento de três retas e eu lhe informo se é possível ou não construir um triângulo com elas.')
a = float(input('Reta 1:'))
b = float(input('Reta 2:'))
c = float(input('Reta 3:'))
print('Processando dados, por favor aguarde...')
sleep(2)
if a < b + c and b < a + c and c < a + b and a == b == c:
    print(f'Com as medidas {a}, {b} e {c} é possível formar um triângulo equilátero.')
elif a < b + c and b < a + c and c < a + b and a == b != c:
    print(f'Com as medidas {a}, {b} e {c} é possível formar um triângulo isósceles.')
elif a < b + c and b < a + c and c < a + b and a == c != b:
    print(f'Com as medidas {a}, {b} e {c} é possível formar um triângulo isósceles.')
elif a < b + c and b < a + c and c < a + b and b == c != a:
    print(f'Com as medidas {a}, {b} e {c} é possível formar um triângulo isósceles.')
elif a < b + c and b < a + c and c < a + b and a != b != c:
    print(f'Com as medidas {a}, {b} e {c} é possível formar um triângulo escaleno.')
else:
    print(f'Com as medidas {a}, {b} e {c} não é possível formar um triângulo.')
