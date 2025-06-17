def calcular_media_anual():
	nota_primeiro_bimestre = float(input('Primeiro bimestre: '))
	nota_segundo_bimestre = float(input('Segundo bimestre: '))
	nota_terceiro_bimestre = float(input('Terceiro bimestre: '))
	nota_quarto_bimestre = float(input('Quarto bimestre: '))
	
	soma_total = nota_primeiro_bimestre + nota_segundo_bimestre + nota_terceiro_bimestre + nota_terceiro_bimestre
	
	print(f'A média do aluno é {soma_total/4}')
	
calcular_media_anual()
