from math import fmod

num = int(input('Me diga um número qualquer: '))
teste = fmod(num, 2)

if teste == 0:
    print('O número {} é PAR'.format(num))
else:
    print('O número {} é ÍMPAR'.format(num))
