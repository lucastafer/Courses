# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. 
# Ex: n = leiaInt('Digite um n: ')

def leiaInt(msg):
    print('~' * 30)
    ok = False #Começa com False, pois "por enquanto não está ok". Após a verificação aí colocaremos True.
    valor = 0
    while True:
        n = str(input(msg)).strip()
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[1:97:41m ERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número inteiro:')
print(f'Você acabou de digitar o número {n}')
