distancia = float(input('Qual é a distância da sua viagem? '))
valor = distancia * 0.5

if distancia >= 200:
    valor = distancia * 0.45

print(f'''
Você está prestes a começar uma viagem de {distancia:.1f}Km.
E o preço da sua passagem será de R${valor:.2f}
''')
