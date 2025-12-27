print('Exercício 017 - Catetos e Hipotenusas')
print(' ')

from math import hypot


def calcular_hipotenusa(cateto_oposto, cateto_adjacente):
    hipotenusa = hypot(cateto_oposto, cateto_adjacente)
    print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))

cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))

calcular_hipotenusa(cateto_oposto, cateto_adjacente)
