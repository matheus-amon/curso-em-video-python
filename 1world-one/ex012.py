print('Exercício 011 - Calculando Descontos')
print(' ')

valor_produto = float(input('Qual o preço do produto? R$'))

valor_desconto = valor_produto - (valor_produto * 0.05)

print(f'O produto que custava R${valor_produto}, na promoção com desconto de 5% vai custar R${valor_desconto:.2f}')
