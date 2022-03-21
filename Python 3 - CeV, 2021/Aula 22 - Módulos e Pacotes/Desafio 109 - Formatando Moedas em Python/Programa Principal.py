# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

import Moeda109

p = float(input('Digite um preço: R$ '))
print(f'A metade de {Moeda109.moeda(p)} é {Moeda109.metade(p, True)}')
print(f'O dobro de {Moeda109.moeda(p)} é {Moeda109.dobro(p, True)}')
print(f'Aumentando 10% temos {Moeda109.aumentar10(p, 10, True)}')
print(f'Descontando 15% temos {Moeda109.diminuir15(p, 15, True)}')
