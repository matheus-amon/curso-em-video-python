casa = float(input('Valor da casa: R$'))
salario = float(input('Salário: R$'))
anos = int(input('Em quantos anos? '))
juros = casa * 2.6
parcela = juros / (anos * 12)

print(f'Para pagar uma casa de R${casa} em {anos} anos a prestação será de R${parcela:.2f}.')

if parcela > salario * 0.3:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo pode ser CONCEDIDO!')
