# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input('Digite um valor em metros.'))
cm = m * 100
mm = m * 1000
print('{} metros corresponde a {} centímetros e {} milímetros.'.format(m, cm, mm))
