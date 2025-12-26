from dataclasses import dataclass
from enum import Enum


class Gender(Enum):
    male = 'M'
    female = 'F'


@dataclass
class People:
    name: str
    age: int
    gender: Gender


class Report:
    def __init__(self, list_of_people: list[People]):
        self.list_of_people = list_of_people
        self.ages: list[int] = [people.age for people in self.list_of_people]

    def calculate_age_mean(self) -> float:
        return float(sum(self.ages) / len(self.ages))

    def get_older_man_name(self) -> str:
        men = [p for p in self.list_of_people if p.gender == Gender.male]
        if not men:
            return "Nenhum homem no grupo"

        oldest = max(men, key=lambda p: p.age)
        return oldest.name

    def count_women_under_20(self) -> int:
        return sum(
            1 for p in self.list_of_people
            if p.gender == Gender.female and p.age < 20
        )


def get_peoples(number_of_people: int):
    peoples: list[People] = []

    for i in range(1, number_of_people + 1):
        print(f'## {i}º Pessoa')
        name: str = input('Digite o nome da pessoa: ')
        age: int = int(input('Digite a idade da pessoa: '))
        gender_input = input("Digite o sexo (M/F): ").upper()
        gender = Gender.male if gender_input == "M" else Gender.female
        print('========================')
        people: People = People(name, age, gender)
        peoples.append(people)

    return peoples

if __name__ == '__main__':
    peoples: list[People] = get_peoples(4)
    report: Report = Report(peoples)
    age_mean: float = report.calculate_age_mean()
    older_man_name: str = report.get_older_man_name()
    number_of_women_under_20: int = report.count_women_under_20()

    print(f'A média de idade do grupo é {age_mean:.2f}')
    print(f'O nome do homem mais velho é {older_man_name}')
    print(f'A quantidade de mulheres com menos de 20 anos é {number_of_women_under_20}')
