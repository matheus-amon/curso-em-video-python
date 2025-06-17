print('Execício 022 - Tocando um MP3')
print(' ')

nome = str(input('Digite seu nome completo: '))
primeiro = nome.split()[0]

print('Analisando seu nome...')

print(f'''
Seu nome em maiúsculas é {nome.upper()}
Seu nome em minúsculas é {nome.lower()}
Seu nome tem ao todo {len(nome) - nome.count(' ')}
Seu primeiro nome é {primeiro} e ele tem {len(primeiro)} letras
''')
