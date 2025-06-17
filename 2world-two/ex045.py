from random import choice
from time import sleep

print(f'''
Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA 
''')

option = int(input('Qual é a sua jogada? '))

user = ''
if option == 0:
    user = 'PEDRA'

elif option == 1:
    user = 'PAPEL'
    
elif option == 2:
    user = 'TESOURA'
    
else:
    print('Escolha inválida')

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

computer = choice(['PEDRA', 'PAPEL', 'TESOURA'])

print(f'''
{'-=' * 10}
Computador jogou {computer}
Jogador jogou {user}
{'-=' * 10}
''')

win = ''
if computer == user:
    win = 'EMPATE!'

elif computer == 'PEDRA' and user == 'TESOURA':
    win = 'COMPUTADOR VENCE'

elif computer == 'PEDRA' and user == 'PAPEL':
    win = 'JOGADOR VENCE'
    
elif computer == 'TESOURA' and user == 'PEDRA':
    win = 'JOGADOR VENCE'
    
elif computer == 'TESOURA' and user == 'PAPEL':
    win = 'COMPUTADOR VENCE'
    
elif computer == 'PAPEL' and user == 'TESOURA':
    win = 'JOGADOR VENCE'
    
elif computer == 'PAPEL' and user == 'PEDRA':
    win = 'COMPUTADOR VENCE'

print(win)
