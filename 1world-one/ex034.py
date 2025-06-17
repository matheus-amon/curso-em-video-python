salario = float(input('Digite o seu salário: R$'))
aumento = 0.1

if salario <= 1430:
    aumento = 0.15

print(f'''
PARABÉNS! Você vai ganhou um aumento de {int(aumento * 100)}%.
Seu salário agora é R${salario + (salario * aumento)}.
''')
