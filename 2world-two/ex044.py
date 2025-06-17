amount = float(input('Qual foi o preço da compra? '))
interest = amount * 0.2
payment_type = int(input('''
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] em até 2x no cartão
[ 4 ] 3x ou mais no cartão
'''))
discount = 0.1

if payment_type == 1:
    print(f'O valor deu R${amount - (amount * discount):.2f}')
   
elif payment_type == 2:
    discount = 0.05
    print(f'O valor deu R${amount - (amount * discount):.2f}')
    
elif payment_type == 3:
    print(f'O valor deu R${amount:.2f}')
    print(f'A parcela ficará R${amount / 2:.2f}')
    
elif payment_type == 4:
    parcels = int(input('Em quantas parcelas você quer? '))
    print(f'O valor deu R${amount + interest:.2f}')
    print(f'A parcela ficará R${(amount + interest) / parcels:.2f}')
    
else:
    print('Digite uma opção válida!')
    