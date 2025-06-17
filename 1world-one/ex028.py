import random
from time import sleep

print('''
-------------------------------------------------------
Vou pensar em um número entre 0 e 5. Tente adivinhar...
-------------------------------------------------------
''')

think_num = random.randint(0, 5)
user_num = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)

if user_num == think_num:
    print('PARABÉNS! Você conseguiu me vencer')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'. format(think_num, user_num))
