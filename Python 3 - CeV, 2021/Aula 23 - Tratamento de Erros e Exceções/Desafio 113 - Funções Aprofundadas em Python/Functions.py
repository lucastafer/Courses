def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1:31mErro: por favor, digite um número inteiro válido.\033[m')
            continue
        else:
            return valor


def leiaFloat(msg):
    while True:
        try:
            valor = float(input(msg))
        except (ValueError, TypeError):
            print('\033[1:31mErro: por favor, digite um número real válido.\033[m')
            continue
        else:
            return valor
