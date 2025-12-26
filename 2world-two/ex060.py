class Solution:
    def __init__(self, number) -> None:
        self.number = int(number)
        self.list: list = []
        self.result: int = 1

    def calculate_factorial(self):
        temp = self.number

        while temp > 0:
            self.list.append(temp)
            self.result *= temp
            temp -= 1

    def show_result(self):
        print(self.list)
        print(self.result)

if __name__ == '__main__':
    number = input('Digite o número: ')
    solution: Solution = Solution(number)

    solution.calculate_factorial()
    solution.show_result()
