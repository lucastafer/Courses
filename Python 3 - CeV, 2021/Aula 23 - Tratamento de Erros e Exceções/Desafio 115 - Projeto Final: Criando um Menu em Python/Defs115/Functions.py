def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def linha(tam=42):
    return '\033[1:36m-' * tam


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[1:97m{c} - {item}\033[m')
        c += 1
    print(linha())
    escolha = leiaInt('\033[1:32mSua opção: \033[m')
    return escolha


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1:31mErro: por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[1:31mUsuário preferiu não digitar esse número.')
            return 0
        else:
            return n
