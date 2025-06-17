print('Execício 023 - Separando dígitos de um número')
print(' ')

while True:
    num = int(input('Infome um número inteiro na casa do milhar: '))
    if num > 9999 or num < 1000:
        print('Insira um número válido')
    else:
        print('Analisando o número {}'.format(num))
        break

n = str(num)

print(f'''
Unidade: {n[3]}
Dezena: {n[2]}
Centena: {n[1]}
Milhar: {n[0]}
''')
