# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida+

print('''Quer descobrir seu IMC? Insira seu peso e sua altura nos campos abaixo e compare com os índices da tabela.
Importante: siga os exemplos e use pontos como separadores.''')
print('Ex: Altura: 1.75')
altura = float(input('Altura:'))
print('Ex: Peso: 75')
peso = float(input('Peso:'))
IMC = peso/ (altura *altura)
if IMC < 18.5:
    print('Seu IMC é {:.1f}, portando você está abaixo do peso.'.format(IMC))
elif IMC < 25:
    print('Seu IMC é {:.1f}, portanto você está no seu peso ideal.'.format(IMC))
elif IMC < 30:
    print('Seu IMC é {:.1f}, portanto você está com sobrepeso.'.format(IMC))
elif IMC < 40:
    print('Seu IMC é {:.1f}, portanto você está com obesidade.'.format(IMC))
elif IMC > 40:
    print('Seu IMC é {:.1f}, portanto você está com obesidade mórbida.'.format(IMC))
