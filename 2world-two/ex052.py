num = int(input('numero: '))
tot = 0

for c in range(1, num+1):
    if num % c == 0:
        tot += 1
    
    print(f'{c}', end=' ')
    
if tot == 2:
    print('é num primo')
else:
    print('n é num primo')
    