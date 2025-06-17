print('Execício 024 - Verificando as primeiras letras de um texto')
print(' ')

cidade = str(input('Nome da cidade: ')).strip().lower()
correta = 'santo'
teste = cidade[:5].strip()

if teste == correta:
    print('correto')
else:
    print('errado')

print(cidade)
