#!/usr/bin/env python3

class Plant():
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def show(self, prefix: str = "Plant created") -> None:
        print(f"{prefix}: {self._name.capitalize()}: "
              f"{round(self._height, 1)}cm, {self._age} days old")

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
            self._age = new_age
            print(f"Age updated: {self._age} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age


def ft_garden_security() -> None:
    plant1 = Plant("rose", 15.0, 10)

    print("=== Garden Security System ===")
    plant1.show()
    print("")
    plant1.set_height(25.0)
    plant1.set_age(30)
    print("")
    plant1.set_height(-5.0)
    plant1.set_age(-1)
    print("")
    plant1.show("Current state")


if __name__ == "__main__":
    ft_garden_security()
