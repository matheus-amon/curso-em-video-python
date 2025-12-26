from datetime import date

years: list = []
for y in range(1, 8):
    year = input(f'ano da {y}º pessoa: ')
    year = int(year)
    years.append(year)

m: int = 0
for y in years:
    current_year = date.today().year
    current_year = int(current_year)
    age = current_year - y

    if age < 18:
        m += 1

print(f'''
{m} menores
{len(years) - m} maiores
''')
