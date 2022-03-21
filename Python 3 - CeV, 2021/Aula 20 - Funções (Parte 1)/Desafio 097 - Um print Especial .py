# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(txt):
    print('~' * (len(txt) + 4))
    print(f'  {txt}')
    print('~' * (len(txt) + 4))


escreva('Curso em Vídeo Python')
print()
escreva('Aprenda Python')
print()
escreva('Edílsonnnn 41 anos')
