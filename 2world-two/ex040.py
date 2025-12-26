def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

while True:
    first_result = input('Primeira nota: ')
    second_result = input('Segunda nota: ')
    thirdy_result = input('Terceira nota: ')

    if isfloat(first_result) and isfloat(second_result) and isfloat(thirdy_result):
        first_result = float(first_result)
        second_result = float(second_result)
        thirdy_result = float(thirdy_result)
        break
    else:
        print('ERROR: "Insira notas válidas"')

mean = (first_result + second_result + thirdy_result) / 3

if mean < 5:
    print(f'Sua média foi {mean:.2f}. REPROVADO!')
elif mean >= 5 and mean <= 6.9:
    print(f'Sua média foi {mean:.2f}. RECUPERAÇÃO!')
else:
    print(f'Sua média foi {mean:.2f}. APROVADO!')
