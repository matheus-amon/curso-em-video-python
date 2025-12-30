class Solution:
	def __init__(self) -> None:
		self.lon: list = []
		self.count_n: int = 0

	def add_in_list(self, n: int) -> None:
		if n != 999:
			self.lon.append(n)
			self.count_n += 1


if __name__ == '__main__':
	solution = Solution()

	while True:
		n = input('Digite um número [999 para parar]: ').strip()
		n = int(n)

		solution.add_in_list(n)

		if n == 999:
			break

	print(f'Você digitou {solution.count_n} números e a soma entre eles foi {sum(solution.lon)}.')
