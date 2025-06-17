print('Exercício 005: Antecessor e Sucessor')

while True:
    numero = input('Digite um número (ou "sair" para encerrar): ')

    if numero.lower() == 'sair':
        print('Programa encerrado.')
        break

    if numero.isnumeric():
        numero = int(numero)
        print(f'''
            O antecessor de {numero} é {numero - 1}
            O sucessor de {numero} é {numero + 1}
        ''')
    else:
        print('Digite um numero válido.')
