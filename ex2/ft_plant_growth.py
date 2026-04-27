#!/usr/bin/env python3

class Plant():
    name = ""
    height = 0.0
    plant_age = 0

    def show(self) -> None:
        print(f"{self.name.capitalize()}: "
              f"{round(self.height, 1)}cm, {self.plant_age} days old")

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.plant_age += 1


def ft_plant_growth() -> None:

    plant1 = Plant()
    plant1.name = "Rose"
    plant1.height = 25.0
    plant1.plant_age = 30

    initial_height = plant1.height

    print("=== Garden Plant Growth ===")
    plant1.show()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        plant1.grow()
        plant1.age()
        plant1.show()

    total = round(plant1.height - initial_height, 1)
    print(f"Growth this week: {total}cm")

if __name__ == "__main__":
    ft_plant_growth()
