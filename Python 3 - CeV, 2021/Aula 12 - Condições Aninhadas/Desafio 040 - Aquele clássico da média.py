# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

P1 = float(input('NOTA P1:'))
P2 = float(input('NOTA P2:'))
MEDIA = (P1 + P2) / 2
if MEDIA < 5.0:
    print('MÉDIA FINAL: {:.2f}\nSITUAÇÃO: REPROVADO'.format(MEDIA))
elif MEDIA >= 5.0 and MEDIA < 7.0:
    print('MÉDIA FINAL: {:.2f}\nSITUAÇÃO: RECUPERAÇÃO.'.format(MEDIA))
elif MEDIA >= 7.0:
    print('MÉDIA FINAL: {:.2f}\nSITUAÇÃO: APROVADO.'.format(MEDIA))
