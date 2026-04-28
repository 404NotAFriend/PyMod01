#!/usr/bin/env python3


class Plant():
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._plant_age = age

    def show(self, prefix: str = "") -> None:
        if prefix:
            prefix = f"{prefix}: "
        else:
            prefix = ""
        print(f"{prefix}{self._name.capitalize()}: "
              f"{round(self._height, 1)}cm, {self._plant_age} days old")

    def set_height(self, new_height: float) -> None:
        if new_height < 0.0:
            print(f"{self._name.capitalize()}: "
                  "Error, height can't be negative")
            print("Height update rejected")
            return
        else:
            self._height = new_height
            print(f"Height updated: {round(self._height, 1)}cm")

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")
            return
        else:
            self._plant_age = new_age
            print(f"Age updated: {self._plant_age} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._plant_age


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._bloomed = False

    def show(self, prefix: str = "") -> None:
        super().show(prefix)
        print(f" Color: {self._color}")
        if self._bloomed:
            print(f" {self._name.capitalize()} is blooming beautifully!")
        else:
            print(f" {self._name.capitalize()} has not bloomed yet")

    def bloom(self) -> None:
        self._bloomed = True


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def show(self, prefix: str = "") -> None:
        super().show(prefix)
        print(f" Trunk diameter: {self._trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self._name.capitalize()} now produces a shade of "
              f"{self._height}cm long and {self._trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 age: int, harvest_season: str,
                 nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def show(self, prefix: str = "") -> None:
        super().show(prefix)
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")

    def grow(self) -> None:
        self._height += 2.1
        self._nutritional_value += 1

    def age(self) -> None:
        self._plant_age += 1


def ft_plant_types() -> None:
    plant1 = Flower("rose", 15.0, 10, "red")
    tree1 = Tree("oak", 200.0, 365, 5.0)
    vegeta1 = Vegetable("tomato", 5.0, 10, "April", 0)

    print("=== Garden Plant Types ===")
    print("=== Flower")
    plant1.show()
    plant1.bloom()
    print("[asking the rose to bloom]")
    plant1.show()
    print("")
    print("=== Tree")
    tree1.show()
    print("[asking the oak to produce shade]")
    tree1.produce_shade()
    print("")
    print("=== Vegetable")
    vegeta1.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(20):
        vegeta1.grow()
        vegeta1.age()
    vegeta1.show()


if __name__ == "__main__":
    ft_plant_types()
