print('Execício 020 - Sorteando uma ordem na lista')
print(' ')

from random import shuffle

primeiro_aluno = input('Primeiro aluno: ')
segundo_aluno = input('Segundo aluno: ')
terceiro_aluno = input('Terceiro aluno: ')
quarto_aluno = input('Quarto aluno: ')

lista = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]
shuffle(lista)

print(f'''
A ordem de apresentação será
{lista}
''')
