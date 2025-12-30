class Solution:
	def __init__(self, n: int) -> None:
		self.n: int = n

	def show_multiplication_table(self) -> None:
		print(f'##### Tabuada de {self.n} #####')

		for n in range(1, 11):
			print(f'{self.n} x {n} = {self.n * n}')

		print('-' * 20)


if __name__ == '__main__':
	while True:
		n = int(input('Quer ver a tabuada de qual valor? ').strip())

		if n < 0:
			break

		solution = Solution(n)
		solution.show_multiplication_table()

	print('Programa de tabuada encerrado. Volte sempre!')
