height = float(input('Qual é a sua altura? '))
weight = float(input('Qual é o seu peso? '))
imc = weight / (height ** 2)

status = ''
if imc > 40:
    status = 'com OBESIDADE MÓRBIDA!'
elif imc >= 30:
    status = 'com OBESIDADE!'
elif imc >= 25:
    status = 'com SOBREPESO!'
elif imc >= 18.5:
    status = 'com o PESO IDEAL!'
else:
    status = 'ABAIXO DO PESO!'

print(f'Você está {status}!')    
