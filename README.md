<div align="center">

*This project has been created as part of the 42 curriculum by bramalho*

<!-- Animated Header -->
<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Activities/Trophy.png" width="80"/>

# 🌿 PyMod1 - Code Cultivation

<img src="https://img.shields.io/badge/Circle-1-00BABC?style=for-the-badge&logo=42&logoColor=white"/>
<img src="https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/42-Porto-000000?style=for-the-badge&logo=42&logoColor=white"/>
<img src="https://img.shields.io/badge/Exercises-7-success?style=for-the-badge"/>

**Object-Oriented Garden Systems — where code blossoms into architecture! 🌸**

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="600"/>

</div>

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Light%20Bulb.png" width="25"/> About The Project

**PyMod1** is the second step of your Python journey at 42! Building on the fundamentals from PyMod0, this module dives deep into **Object-Oriented Programming** through a comprehensive digital garden ecosystem.

Through 7 exercises you'll learn:
- 🏗️ **Classes & Instances** — blueprints and objects
- 🔒 **Encapsulation** — protecting data with getters and setters
- 👨‍👩‍👧 **Inheritance** — reusing code through parent/child classes
- 🔁 **Method Overriding** — customizing inherited behavior with `super()`
- 🏭 **Constructors** — initializing objects with `__init__`
- 📊 **Static & Class Methods** — `@staticmethod` and `@classmethod`
- 🪆 **Nested Classes** — classes inside classes for data grouping

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Rocket.png" width="25"/> Exercises

| # | File | Concepts | Description |
|---|------|----------|-------------|
| ex0 | `ft_garden_intro.py` | `if __name__`, shebang | Program entry point and execution |
| ex1 | `ft_garden_data.py` | `class`, `show()` | Plant class with attributes and display method |
| ex2 | `ft_plant_growth.py` | `grow()`, `age()`, `range()` | Simulate plant growth over a week |
| ex3 | `ft_plant_factory.py` | `__init__` | Constructor — create plants in one step |
| ex4 | `ft_garden_security.py` | `_protected`, getters/setters | Encapsulation and data validation |
| ex5 | `ft_plant_types.py` | `super()`, inheritance | Flower, Tree and Vegetable subclasses |
| ex6 | `ft_garden_analytics.py` | `@staticmethod`, `@classmethod`, nested classes | Full OOP system with stats tracking |

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Gear.png" width="25"/> Technical Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flake8](https://img.shields.io/badge/flake8-linted-success?style=for-the-badge)
![Mypy](https://img.shields.io/badge/mypy-typed-blue?style=for-the-badge)

Pure Python 3.10+ — no external libraries. Validated with `flake8` and `mypy`.

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/File%20Folder.png" width="25"/> Project Structure

```
PyMod1/
├── ex0/
│   └── ft_garden_intro.py        # Program entry point & shebang
├── ex1/
│   └── ft_garden_data.py         # Plant class with show()
├── ex2/
│   └── ft_plant_growth.py        # Growth simulation over a week
├── ex3/
│   └── ft_plant_factory.py       # Constructor & plant factory
├── ex4/
│   └── ft_garden_security.py     # Encapsulation & validation
├── ex5/
│   └── ft_plant_types.py         # Inheritance — Flower, Tree, Vegetable
└── ex6/
    └── ft_garden_analytics.py    # Analytics — static/class methods, nested classes
```

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Hammer%20and%20Wrench.png" width="25"/> Getting Started

### Prerequisites

- Python 3.10+ (`python3 --version`)
- flake8 (`pip install flake8 --break-system-packages`)
- mypy (`pip install mypy --break-system-packages`)

### Clone & Run

```bash
# Clone the repository
git clone https://github.com/404NotAFriend/PyMod1.git
cd PyMod1

# Run any exercise directly
python3 ex6/ft_garden_analytics.py

# Or with execute permission
chmod +x ex6/ft_garden_analytics.py
./ex6/ft_garden_analytics.py
```

### Validate Code Quality

```bash
flake8 ex6/ft_garden_analytics.py
mypy ex6/ft_garden_analytics.py
```

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Memo.png" width="25"/> Key Concepts Explained

### ex0 — Program Entry Point
```python
#!/usr/bin/env python3

if __name__ == "__main__":
    ft_garden_intro("rose", 25, 30)
```
The shebang lets you run `./ft_garden_intro.py` directly. The `if __name__` guard ensures code only runs when executed directly, not when imported.

---

### ex1 & ex3 — Class vs Constructor
```python
# ex1 — two steps
plant = Plant()
plant.name = "Rose"

# ex3 — one step with __init__
plant = Plant("Rose", 25.0, 30)
```
`__init__` is the constructor — it runs automatically when an instance is created.

---

### ex4 — Encapsulation
```python
class Plant():
    def __init__(self, name: str, height: float) -> None:
        self._name = name      # protected — don't access directly
        self._height = height

    def set_height(self, value: float) -> None:
        if value < 0:          # validate before setting
            print("Error: height can't be negative")
            return
        self._height = value
```
`_protected` attributes signal "use the getter/setter instead". Think of it as a warning sign 🚧 — not a hard block, but a strong suggestion.

---

### ex5 — Inheritance & super()
```python
class Flower(Plant):           # inherits everything from Plant
    def __init__(self, name: str, height: float,
                 age: int, color: str) -> None:
        super().__init__(name, height, age)  # Plant handles these
        self._color = color                  # Flower adds this

    def show(self, prefix: str = "") -> None:
        super().show(prefix)   # reuse Plant's show()
        print(f" Color: {self._color}")  # then add extra info
```
`super()` calls the parent class method — write once, reuse everywhere.

---

### ex6 — Static & Class Methods
```python
@staticmethod
def is_older_than_year(age: int) -> bool:
    return age > 365           # no self needed — just a utility

@classmethod
def create_anonymous(cls) -> "Plant":
    return cls("unknown plant", 0.0, 0)  # alternative constructor
```

And nested classes for grouping related data:
```python
class Plant():
    class Stats():             # lives inside Plant
        def __init__(self) -> None:
            self._grow_count = 0
            self._show_count = 0
```

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Pushpin.png" width="25"/> Common Pitfalls

| ❌ Issue | ✅ Solution |
|---------|------------|
| `capitalize` without `()` | `self._name.capitalize()` not `self._name.capitalize` |
| Accessing `_protected` directly | Use `get_height()` / `set_height()` instead |
| Forgetting `self` in methods | Every method needs `self` as first parameter |
| Method name conflicts with attribute | Rename attribute e.g. `_plant_age` to free up `age()` |
| `super()` not called in subclass `__init__` | Always call `super().__init__()` first |
| mypy type mismatch `int` vs `float` | Use `0.0` not `0` for float attributes |

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Star-Struck.png" width="25"/> What's Next?

After mastering PyMod1, you'll move on to:
- 📦 **PyMod2** — Modules, imports and file I/O
- 📊 **Data Science** modules — NumPy, Pandas, and beyond
- 🤖 **ML/AI** modules — the future of the 42 curriculum!

OOP is the foundation of modern software — you've just built it from scratch! 🌿

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Link.png" width="25"/> Resources

- [Python 3 Official Docs](https://docs.python.org/3/)
- [OOP in Python — Real Python](https://realpython.com/python3-object-oriented-programming/)
- [Type Hints — PEP 484](https://peps.python.org/pep-0484/)
- [flake8 docs](https://flake8.pycqa.org/)
- [mypy docs](https://mypy.readthedocs.io/)
- [42 Intranet](https://intra.42.fr)

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Mobile%20Phone.png" width="25"/> Contact

**Bruno Gomes** — 42 Porto Student

[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:brunodrcgomes@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/meetbrunogomes/)
[![42](https://img.shields.io/badge/42-000000?style=for-the-badge&logo=42&logoColor=white)](https://profile.intra.42.fr/users/bramalho)

---

<div align="center">

### 💡 Pro Tips from Development

<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Nerd%20Face.png" width="20"/> **Always run flake8 AND mypy** — they catch different types of problems

<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Food/Hot%20Beverage.png" width="20"/> **Call `super().__init__()` first** — always, in every subclass

<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Star-Struck.png" width="20"/> **Think before you code** — draw the inheritance tree on paper first

<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Smiling%20Face%20with%20Sunglasses.png" width="20"/> **`_protected` is a warning, `__private` is a wall** — choose wisely

<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Exploding%20Head.png" width="20"/> **`self` is always the specific instance** — never forget that

</div>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer"/>

**Thanks for checking out PyMod1! From classes to inheritance chains — one object at a time.** 🌿

<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand%20gestures/Waving%20Hand.png" width="40"/>

*"A class is just a blueprint — the magic happens when you build something with it."*

### 💻 Built with dedication at 42 School Porto

</div>
