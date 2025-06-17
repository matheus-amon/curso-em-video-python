from datetime import datetime

current_year = datetime.today().year
birthday = input('Insira sua data de nascimento: ').strip()
year = int(birthday[6:])
age = current_year - year
info = 'Sua categoria é '

if age > 6  and age <= 9:
    category = 'MIRIM!'
elif age > 9 and age <= 14:
    category = 'INFANTIL!'
elif age > 14 and age <= 19:
    category = 'JUNIOR!'
elif age > 19 and age <= 25:
    category = 'SÊNIOR!'
elif age > 25 and age <= 50:
    category = 'MASTER!'
else:
    info = 'Infelizmente você não se enquadra em nenhuma categoria'
    category = '!'
    
print(info + category)
