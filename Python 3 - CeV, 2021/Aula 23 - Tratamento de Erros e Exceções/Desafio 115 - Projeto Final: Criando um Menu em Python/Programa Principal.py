# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
# O sistema deve ter somente duas opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

from Defs115 import Functions
from Defs115 import Arquivo
from time import sleep

arq = 'Cadastro.txt'

if not Arquivo.arquivoExiste(arq):
    Arquivo.criarArquivo(arq)

while True:
    resposta = Functions.menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        Arquivo.lerArquivo(arq)
    elif resposta == 2:
        Functions.cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).title()
        idade = Functions.leiaInt('Idade: ')
        Arquivo.cadastrar(arq, nome, idade)
    elif resposta == 3:
        Functions.cabeçalho('Saindo do sistema...')
        sleep(2)
        Functions.cabeçalho('Até logo!')
        break
    else:
        print('\033[31mErro: digite uma opção válida.\033[m')
