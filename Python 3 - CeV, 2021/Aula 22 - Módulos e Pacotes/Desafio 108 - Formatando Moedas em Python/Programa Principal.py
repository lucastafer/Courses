# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

import Moeda108

preço = float(input('Digite um preço: R$ '))
print(f'O dobro de {Moeda108.moeda(preço)} é {Moeda108.dobro(preço)}')
print(f'A metade de {Moeda108.moeda(preço)} é {Moeda108.metade(preço)}')
print(f'{Moeda108.moeda(preço)} com 10% de aumento fica {Moeda108.aumentar10(preço)}')
print(f'{Moeda108.moeda(preço)} com 10% de desconto fica {Moeda108.diminuir10(preço)}')
