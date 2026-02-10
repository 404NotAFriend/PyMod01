class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def display_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 100, 365)
    tulip = Plant("Tulip", 15, 20)

    print('""" Garden Plant Registry """')
    rose.display_info()
    oak.display_info()
    tulip.display_info()
