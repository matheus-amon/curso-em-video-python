# %%
number1 = int(input('Digite um numero: ').strip())
number2 = int(input('Digite outro numero: ').strip())

# %%
OPTIONS = """
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
 """

# %%
while True:
    option: int = int(input(f'Escolha o que quer fazer: \n {OPTIONS} \n -> '))

    if option == 5:
        print('Programa fechado')
        break

    if option == 1:
        result = number1 + number2
        print(result)

    if option == 2:
        result = number1 * number2
        print(result)

    if option == 3:
        result = [number1, number2]
        print(max(result))

    if option == 4:
        number1 = int(input('Digite um numero: ').strip())
        number2 = int(input('Digite outro numero: ').strip())
