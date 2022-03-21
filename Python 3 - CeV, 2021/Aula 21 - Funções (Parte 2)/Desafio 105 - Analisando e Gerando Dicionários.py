# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.


def notas(*num, sit=False):
    """
    Função para analisar notas e situações de diversos alunos.
    :param num: uma ou mais notas (aceita várias)
    :param sit: situação (opcional)
    :return: dict com a maior e menor nota, média da turma e a situação do aluno (opcional).
    """
    r = {}
    r['Total'] = len(num)
    r['Maior'] =  max(num)
    r['Menor'] = min(num)
    r['Média'] = sum(num)/len(num)
    if sit:
        if r['Média'] > 7:
            r['Situação'] = 'BOA'
        elif r['Média'] >=5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'
    return r


resp = notas(5.5, 7.5, 8.5, sit=True)
print(resp)
help(notas)
