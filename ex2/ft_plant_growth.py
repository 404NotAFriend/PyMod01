class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height += 1

    def age_one_day(self) -> None:
        self.age += 1

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    print('""" Day 1 """')
    print(rose.get_info())
    print('""" Day 7 """')
    for _ in range(6):
        rose.grow()
        rose.age_one_day()
    print(rose.get_info())
    print(f"Growth this week: +{rose.height - 25}cm")
