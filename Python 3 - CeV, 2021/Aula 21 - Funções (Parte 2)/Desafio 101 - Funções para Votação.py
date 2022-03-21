# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


def voto(idade):
    r1 = "obrigatório"
    r2 = "negado, proibido votar"
    r3 = "opcional"
    if idade >= 18 and idade < 65:
        return r1
    elif idade < 16:
        return r2
    elif idade < 18 and idade >= 16 or idade >= 65:
        return r3


ano = int(input('Ano de nascimento: '))
idade = 2021 - ano
r = voto(idade)
print(f'Com {idade} anos o voto é {r}.')
