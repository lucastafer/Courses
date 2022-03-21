def aumentar10(p = 0, taxa = 10, formato = False):
    res = p * 1.10
    return res if formato is False else moeda(res)


def diminuir15(p = 0, taxa = 15, formato = False):
    res = p * 0.90
    return res if formato is False else moeda(res)


def dobro(p = 0, formato = False):
    res = p * 2
    return res if formato is False else moeda(res)


def metade(p = 0, formato = False):
    res = p / 2
    return res if formato is False else moeda(res)


def moeda(preço = 0, moeda = 'R$ '):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')
  
