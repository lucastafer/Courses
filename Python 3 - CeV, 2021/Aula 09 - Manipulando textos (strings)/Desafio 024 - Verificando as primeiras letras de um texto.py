# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome de alguma cidade.')).title().split()
x = cidade[0]
print('Santo' in x)

# Opção utilizando if e else
cidade = str(input('Digite o nome de alguma cidade.')).title().split()
if 'Santo' == cidade[0]:
    print('Essa cidade começa com a palavra Santo.')
else:
    print('Essa cidade não começa com a palavra Santo.')
