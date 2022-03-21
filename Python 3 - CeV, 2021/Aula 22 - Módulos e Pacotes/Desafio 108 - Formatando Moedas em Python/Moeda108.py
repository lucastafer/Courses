def aumentar10(preço = 0):
    res = preço * 1.10
    return f'R$ {res:.2f}'.replace('.', ',')


def diminuir10(preço = 0):
    res = preço * 0.90
    return f'R$ {res:.2f}'.replace('.', ',')


def dobro(preço = 0):
    res = preço * 2
    return f'R$ {res:.2f}'.replace('.', ',')


def metade(preço = 0):
    res = preço / 2
    return f'R$ {res:.2f}'.replace('.', ',')


def moeda(preço = 0, moeda = 'R$ '):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
