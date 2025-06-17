num = int(input('Digite um numero para ver sua tabuada: '))

for n in range(1, 11):
    print(f'{num} X {n:2} = {num * n}')
