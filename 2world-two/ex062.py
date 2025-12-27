class Solution:
	def __init__(self, term, razion) -> None:
		self.term = term
		self.razion = razion
		self.total_terms = 0

	def calculate_pa(self):
		pa_count = 0

		while pa_count <= 9:
			print(f'{self.term}', end=' -> ')
			self.term += self.razion
			pa_count += 1
			self.total_terms += 1

		print('PAUSA')

	def continue_calculate_pa(self, terms):
		while terms > 0:
			print(f'{self.term}', end=' -> ')
			self.term += self.razion
			terms -= 1
			self.total_terms += 1

		print('PAUSA')


if __name__ == '__main__':
	term = int(input('Primeiro termo: '))
	razion = int(input('Razão: '))
	solution = Solution(term, razion)

	solution.calculate_pa()

	while True:
		terms = int(input('Quantos termos você quer mostrar mais? '))

		if terms <= 0:
			break

		solution.continue_calculate_pa(terms)

	print(f'Progressão finalizada com {solution.total_terms} termos mostrados.')
