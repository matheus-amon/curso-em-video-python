class Solution:
	def __init__(self, times) -> None:
		self.times: int = times - 2
		self.list: list = [0, 1]

	def __calculate_next_number_in_fibonnaci_sequence(self) -> int:
		result: int = self.list[-2] + self.list[-1]
		self.list.append(result)
		return result

	def while_loop_calculate_fibonnaci_sequence(self) -> None:
		while self.times > 0:
			self.__calculate_next_number_in_fibonnaci_sequence()
			self.times -= 1

	def show_fibonnaci_sequence(self) -> None:
		for n in self.list:
			print(n, end=' -> ')

		print('FIM')

if __name__ == '__main__':
	times: int = int(input('Quantos termos você quer mostrar? '))
	solution: Solution = Solution(times)

	solution.while_loop_calculate_fibonnaci_sequence()
	solution.show_fibonnaci_sequence()
