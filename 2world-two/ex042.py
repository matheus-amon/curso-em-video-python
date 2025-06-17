first_segment = int(input('Primeira reta: '))
second_segment = int(input('Segunda reta: '))
third_segment = int(input('Terceira reta: '))
type = 'TRIÂNGULO!'

if first_segment >= (second_segment + third_segment) or second_segment >= (first_segment + third_segment) or third_segment >= (first_segment + second_segment):
    print('QUE PENA! Essas retas NÃO formam um triângulo')
else:
    if first_segment == second_segment == third_segment:
        type = 'EQUILÁTERO!'
    elif first_segment == second_segment or first_segment == third_segment or second_segment == third_segment:
        type = 'ISÓSCELES!'
    else:
        type = 'ESCALENO!'
    
    print(f'UAU! Essas retas formam um triângulo {type}')
