sum = 0
count = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        count += 1
        sum += n

print('A soma desses {} valores é {}'.format(count, sum))
