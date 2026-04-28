#!/usr/bin/env python3


class Plant():
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._plant_age = age
        self._stats = Plant.Stats()

    def show(self, prefix: str = "") -> None:
        if prefix:
            prefix = f"{prefix}: "
        else:
            prefix = ""
        print(f"{prefix}{self._name.capitalize()}: "
              f"{round(self._height, 1)}cm, {self._plant_age} days old")
        self._stats._show_count += 1

    def grow(self) -> None:
        self._stats._grow_count += 1

    def age(self) -> None:
        self._stats._age_count += 1

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

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("unknown plant", 0.0, 0)

    class Stats():
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def display(self) -> None:
            print(f"Stats: {self._grow_count} grow, "
                  f"{self._age_count} age, "
                  f"{self._show_count} show")


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

    def grow(self) -> None:
        super().grow()
        self._height += 8.0


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._stats: Tree.Stats = Tree.Stats()
        self._trunk_diameter = trunk_diameter

    def show(self, prefix: str = "") -> None:
        super().show(prefix)
        print(f" Trunk diameter: {self._trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self._name.capitalize()} now produces a shade of "
              f"{self._height}cm long and {self._trunk_diameter}cm wide.")
        self._stats._shade_count += 1

    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_count = 0

        def display(self) -> None:
            super().display()
            print(f"{self._shade_count} shade")


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
        super().grow()
        self._height += 2.1
        self._nutritional_value += 1

    def age(self) -> None:
        super().age()
        self._plant_age += 1


class Seed(Flower):
    def __init__(self, name: str, height: float,
                 age: int, color: str, seed_amount: int) -> None:
        super().__init__(name, height, age, color)
        self._max_seeds = seed_amount
        self._seed_amount = 0

    def show(self, prefix: str = "") -> None:
        super().show(prefix)
        print(f" Seeds: {self._seed_amount}")

    def grow(self) -> None:
        super().grow()
        self._height += 22.0

    def bloom(self) -> None:
        super().bloom()
        self._seed_amount = self._max_seeds

    def age(self) -> None:
        super().age()
        self._plant_age += 20


def display_stats(plant: Plant) -> None:
    plant._stats.display()


def ft_garden_analytics() -> None:
    plant1 = Flower("rose", 15.0, 10, "red")
    seed1 = Seed("sunflower", 80.0, 45, "yellow", 42)
    tree1 = Tree("oak", 200.0, 365, 5.0)
    vegeta1 = Vegetable("tomato", 5.0, 10, "April", 0)

    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print("")

    print("=== Flower")
    plant1.show()
    print("[statistics for Rose]")
    display_stats(plant1)
    plant1.grow()
    plant1.bloom()
    print("[asking the rose to grow and bloom]")
    plant1.show()
    print("[statistics for Rose]")
    display_stats(plant1)
    print("")

    print("=== Tree")
    tree1.show()
    print("[statistics for Oak]")
    display_stats(tree1)
    print("[asking the oak to produce shade]")
    tree1.produce_shade()
    print("[statistics for Oak]")
    display_stats(tree1)
    print("")

    print("=== Seed")
    seed1.show()
    print("[make sunflower grow, age and bloom]")
    seed1.grow()
    seed1.age()
    seed1.bloom()
    seed1.show()
    print("[statistics for Sunflower]")
    display_stats(seed1)
    print("")

    print("=== Anonymous")
    anon = Plant.create_anonymous()
    anon.show()
    print("[statistics for Unknown plant]")
    display_stats(anon)


if __name__ == "__main__":
    ft_garden_analytics()
