class Solution:
	def __init__(self, term, razion) -> None:
		self.term = term
		self.razion = razion
		self.result = 0

	def calculate_pa(self):
		pa_count = 0
		while pa_count <= 9:
			print(f'{self.term}', end=' -> ')
			self.term += self.razion
			pa_count += 1

		print('FIM')


if __name__ == '__main__':
	term = int(input('Primeiro termo: '))
	razion = int(input('Razão: '))
	solution = Solution(term, razion)


	solution.calculate_pa()
