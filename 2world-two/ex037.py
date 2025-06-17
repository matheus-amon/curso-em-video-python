num = int(input('Digite um número inteiro: '))

trials = 3

while trials > 0:
    choice = int(input('''
    ''' + "-=-" * 10 + '''
    [ 1 ] Converter em binário.
    [ 2 ] Converter em octal.
    [ 3 ] Converter em hexadecimal.
    ''' + "-=-" * 10 + '''
    Digite sua escolha: '''))

    if choice == 1:
        print(f'BINÁRIO: {bin(num)[2:]}')  # Removendo prefixo '0b'
    elif choice == 2:
        print(f'OCTAL: {oct(num)[2:]}')  # Removendo prefixo '0o'
    elif choice == 3:
        print(f'HEXADECIMAL: {hex(num)[2:].upper()}')  # Removendo '0x' e deixando maiúsculo
    else:
        print(f'Opção inválida!')

    trials -= 1  # Agora trials diminui corretamente
    print(f'Você tem {trials} tentativa(s) restante(s).')

    if trials == 0:
        break

print(f'''
{'-=-' * 10}
ACABOU
{'-=-' * 10}
''')
