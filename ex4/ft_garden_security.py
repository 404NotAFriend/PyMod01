class SecurePlant:
    def __init__(self, name: str) -> None:
        self._name = name
        self._height = 0
        self._age = 0
        print(f"Plant created: {self._name}")

    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        self._height = height
        print(f"Height updated: {height}cm [OK]")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
            return
        self._age = age
        print(f"Age updated: {age} days [OK]")

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_name(self) -> str:
        return self._name

    def display_info(self) -> None:
        print(f"Current plant: {self._name}" +
              f" ({self._height}cm, {self._age} days)")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose")
    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-5)
    print()
    plant.display_info()
