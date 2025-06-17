velocidade = int(input('Qual é a velocidade atual do carro? '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    multado = print(f'''
MULTADO! Você excedeu o limite permitido que é de 80Km/h
Você deve pagar uma multa de R${multa:.2f}!
''')

print('Tenha um bom dia! Dirija com segurança!')
