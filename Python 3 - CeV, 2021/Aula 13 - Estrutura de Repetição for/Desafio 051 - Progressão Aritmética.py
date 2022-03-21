# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
# OBS: an = a1 + (n - 1) . r

print('+' * 22)
print(' 10 TERMOS DE UMA PA')
print('+' * 22)

PT = float(input('Primeiro termo:'))
R = float(input('Razão:'))
n = PT + R
print('Sendo o primeiro termo da PA {:.0f} e a razão {:.0f}, os dez primeiros termos dessa PA são:'.format(PT, R))
for c in range(1, 11):
    n = 0 + (PT + (c-1) * R)
    print('{:.0f}'.format(n), end=' → ')
print('FIM!')
