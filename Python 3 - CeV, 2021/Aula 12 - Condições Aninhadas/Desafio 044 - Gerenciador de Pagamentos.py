# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto;
# - à vista no cartão: 5% de desconto;
# - em até 2x no cartão: preço formal;
# - 3x ou mais no cartão: 20% de juros.

print('================= TAFER STORE =================')
TOTAL = float(input('WELCOME TO TAFER STORE! WHAT IS THE TOTAL VALUE OF YOUR ORDERS ?\n R$'))
print('RIGHT. PLEASE CHOOSE YOUR PAYMENT METHOD:')
PGTO = int(input('[1] CASH DOWN (MONEY OR BANK CHEQUE)\n[2] CASH DOWN (CARD)\n[3] PAY BY 2 INSTALLMENTS ON CREDIT CARD\n[4] PAY BY 3 OR MORE INSTALLMENTS ON CREDIT CARD.'))
if PGTO == 1:
    print('OK! ON CASH DOWN OR BANK CHEQUE YOU RECEIVE AN ADDITIONAL DISCOUNT OF 10%, TOTALIZING R${:.2f}.'.format(TOTAL*0.90))
elif PGTO == 2:
    print('OK! ON CASH DOWN IN CREDIT CARD YOU RECEIVE AN ADDITIONAL DISCOUNT OF 5%, TOTALIZING R${:.2f}.'.format(TOTAL*0.95))
elif PGTO == 3:
    print('OK! PAYING IN UNTIL 2 INSTALLMENTS YOU WON T RECEIVE ANY ADDITIONAL TAX, TOTALIZING R${:.2f}.'.format(TOTAL))
elif PGTO == 4:
    print('ALRIGHT! PAYING IN 3 OR MORE INSTALLMENTS YOU WILL HAVE AN ADDITIONAL TAX OF 20%, TOTALIZING R${:.2f}'.format(TOTAL*1.20))
    PCL = int(input('HOW MANY INSTALLMENTS DO YOU WANT ?'))
    print('RIGHT. IN THAT FORM, YOU WILL PAY {} PAYMENTS OF R${:.2f}.'.format(PCL, (TOTAL*1.20)/PCL))
else:
    print('INVALID PAYMENT METHOD. PLEASE TRY AGAIN.')
