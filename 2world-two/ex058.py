import random
from time import sleep


class NumberProducer:
    def __init__(self) -> None:
        self.number: int = random.randint(0, 10)

    def validate_num(self, user_number_input: int) -> bool:
        return user_number_input == self.number

    def hint(self, user_number_input: int) -> str:
        if user_number_input < self.number:
            return "O número é **maior**."
        else:
            return "O número é **menor**."


def get_user_number_input():
    print('''
-------------------------------------------------------
Vou pensar em um número entre 0 e 10. Tente adivinhar...
-------------------------------------------------------
''')
    number_producer: NumberProducer = NumberProducer()
    user_num: int = int(input('Em que número eu pensei? '))
    print('PROCESSANDO...')
    sleep(1)

    is_valid: bool = number_producer.validate_num(user_number_input=user_num)
    count: int = 0

    while not is_valid:
        print(number_producer.hint(user_num))
        user_num = int(input('Tente novamente: '))
        count += 1
        is_valid = number_producer.validate_num(user_number_input=user_num)

    print(f'Parabéns! Você acertou em {count} tentativas!')


if __name__ == '__main__':
    get_user_number_input()
