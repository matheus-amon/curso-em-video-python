print('Exercício 015 - Aluguel de Carros')
print(' ')

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))

dias = dias * 60
km = km * 0.15

print('O total a pagar é de R${:.2f}'.format(dias+km))
