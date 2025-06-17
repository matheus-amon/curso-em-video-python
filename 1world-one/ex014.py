print('Exercício 014 - Conversor de Temperatura')
print(' ')

temperatura = float(input('Informe a temperatura em °C: '))
convertido = (temperatura * 1.8) + 32

print('A temperatura de {:.1f}°C corresponde a {:.1f}°F!'.format(temperatura, convertido))
