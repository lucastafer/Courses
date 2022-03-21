# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

exp = str(input('Digite uma expressão:'))
lista = [] # Nessa lista aqui vamos pescar todos os parenteses que tiverem na expressão.
for símbolo in exp: # Para cada símbolo na expressão:
    if símbolo == '(': # Se tiver (, eu pesco e jogo na lista.
        lista.append('(')
    elif símbolo == ')': # Se o símbolo for ), antes de pescar eu vejo se o comprimento da lista está maior que zero, pois se tiver algo nela, tenho que tirar.
        if len(lista) > 0:
            lista.pop()   # Cada vez que eu pesquei um parenteses abrindo, eu tirei ele com o que pesquei fechando, pois ele já achou seu par.
        else:
            lista.append(')') # Após verificar com o pop, pode jogar na lista.
            break
if len(lista) == 0: # Se tiver maior que zero é porque algum parenteses nao achou seu par, ai sobrou.
    print('Sua expressão é válida!')
else:
    print('Sua expressão é inválida!')
