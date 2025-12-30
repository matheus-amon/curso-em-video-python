class Solution:
	def __init__(self) -> None:
		self.lon: list[int] = []
		self.non: int = 0

	def average(self) -> float:
		return sum(self.lon) / len(self.lon)

	def add_n(self, n: int) -> None:
		self.lon.append(n)
		self.non += 1

	def get_min_max_n(self) -> list[int]:
		min_n: int = min(self.lon)
		max_n: int = max(self.lon)
		return [min_n, max_n]

if __name__ == '__main__':
	solution = Solution()

	while True:
		n = int(input('Digite um número: ').strip())

		solution.add_n(n)

		cond = input('Quer continuar? [S/N] ').strip().lower()

		if cond == 'n':
			break

	min_max_n = solution.get_min_max_n()

	print(f'Você digitou {solution.non} e a média foi {solution.average()}')
	print(f'O maior valor foi {min_max_n[1]} e o menor foi {min_max_n[0]}')
