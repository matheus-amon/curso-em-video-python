phrase = input('frase: ')
phrase: str = str(phrase.upper().strip().replace(' ', ''))

inverse: str = phrase[::-1]

print(f'{phrase} ao contrario é {inverse}')

if inverse == phrase:
    print('é palindromo')
  