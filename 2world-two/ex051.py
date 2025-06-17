print('=' * 20)
print('    10 TERMOS DE UMA PA    ')
print('=' * 20)

term = int(input('Primeiro termo: '))
razion = int(input('Razão: '))

for n in range(1, 11):
    print(f'{term}', end=' -> ')
    term += razion
    print('ACABOU')
