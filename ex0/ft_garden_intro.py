#!/usr/bin/env python3

def ft_garden_intro(plant_name: str, height: int, age: int) -> None:
    name = plant_name.capitalize()

    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print("")
    print("=== End of Program ===")


if __name__ == "__main__":

    ft_garden_intro("rose", 25, 30)
