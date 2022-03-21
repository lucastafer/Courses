# Crie um módulo chamado Moeda107.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

import Moeda107


n = float(input('Digite um preço: R$'))
print(f'O dobro de R$ {n:.2f} é R$ {Moeda107.dobro(n):.2f}')
print(f'A metade de R$ {n:.2f} é R$ {Moeda107.metade(n):.2f}')
print(f'Um quarto de R$ {n:.2f} é R$ {Moeda107.quarto(n):.2f}')
print(f'R$ {n:.2f} com 10% de aumento fica R$ {Moeda107.aumentar10(n):.2f}')
print(f'R$ {n:.2f} com 10% de desconto fica R$ {Moeda107.diminuir10(n):.2f}')
