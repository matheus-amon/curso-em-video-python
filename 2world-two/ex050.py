print('Digite seis números')

soma = 0
for n in range(1, 7):
    num = int(input(f'{n}. '))
    if num % 2 == 0:
        soma += num

print(f'A soma dos números pares deu {soma}')
