def leiaDinheiro(msg):
    while True:
        valor = input(msg).strip().replace(',', '.')
        if valor.replace('.', '').isnumeric():
            break
        print(f'\033[0:31mERRO: "{valor}" é um preço inválido!\033[m')
    return float(valor)
