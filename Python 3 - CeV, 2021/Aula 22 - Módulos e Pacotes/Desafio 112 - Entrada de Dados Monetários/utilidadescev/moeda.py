def aumentar(p=0, taxa=0):
    res = p * ((taxa/100) + 1)
    return res


def diminuir(p=0, taxa=0):
    res = p * (1.00 - (taxa/100))
    return res


def dobro(p=0):
    res = p * 2
    return res


def metade(p=0):
    res = p / 2
    return res


def moeda(p=0, moeda='R$ '):
    return f'{moeda}{p:>.2f}'.replace('.', ',')


def resumo(p=0, aumento=0, desconto=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(p)}'.replace('.', ','))
    print(f'Dobro do preço: \t{moeda(dobro(p))}'.replace('.', ','))
    print(f'Metade do preço: \t{moeda(metade(p))}'.replace('.', ','))
    print(f'20% de aumento: \t{moeda(aumentar(p, aumento))}'.replace('.', ','))
    print(f'12% de desconto: \t{moeda(diminuir(p, desconto))}'.replace('.', ','))
    print('-' * 30)
    
