print(f'''
{"-=-" * 10}
Analisador de Triângulos
{"-=-" * 10}
''')

freta = int(input('Primeira reta: '))
sreta = int(input('Segunda reta: '))
treta = int(input('Terceira reta: '))

if freta >= (sreta + treta) or sreta >= (freta + treta) or treta >= (freta + sreta):
    print('ERRADO! Essas retas NÃO formam um triângulo')
else:
    print('EXATO! Essas retas formam um triângulo')
    