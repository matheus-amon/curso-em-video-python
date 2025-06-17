print('Execício 018 - Seno, Cosseno e Tangente')
print(' ')

import math

angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'''
O ângulo de {angulo} tem o SENO de {seno:.2f}
O ângulo de {angulo} tem o COSSENO de {cosseno:.2f}
O ângulo de {angulo} tem o TANGENTE de {tangente:.2f}
''')
