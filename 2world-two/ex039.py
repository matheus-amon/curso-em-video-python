import datetime

age = int(input('Informe sua idade: '))
year = datetime.datetime.today().year

if age < 18:
    remainder_years = 18 - age
    year = year + remainder_years
    print(f'Faltam {remainder_years} anos, {year} ta chegando!')

elif age == 18:
    user_response = input('Você já se alistou? [Sim ou Não] ')

    if user_response == 'Sim':
        print('Meus parabéns recruta')
    else:
        print(f'Chegou a sua hora, {year} é o seu ano militar')

else:
    user_response = input('Você já se alistou? [Sim ou Não] ')

    if user_response == 'Não':
        remainder_years = age - 18
        year = year - remainder_years
        print(f'Você deveria ter se alistado em {year}, está atrasado {remainder_years} anos.')
    else:
        print('Meus parabéns soldado')
