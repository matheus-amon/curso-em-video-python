frase = str(input('Digite uma frase: ')).strip()

print(f'''
A letra A aparece {frase.lower().count('a')} vezes na frase.
A primeira letra A apareceu na posição {frase.lower().find('a') + 1}
A última letra A apareceu na posição {frase.lower().rfind('a') + 1}
''')
