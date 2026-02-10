class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


def ft_plant_factory() -> None:
    plant_orders = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]

    print("=== Plant Factory Output ===")

    for order in plant_orders:
        name, height, age = order
        plant = Plant(name, height, age)
        print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")

    print()
    print(f"Total plants created: {len(plant_orders)}")


if __name__ == "__main__":
    ft_plant_factory()
