class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.initial_height = height

    def grow(self, amount: int) -> None:
        self.height += amount

    def age_plant(self) -> None:
        self.age += 1

    def get_info(self) -> str:
        name_cap = self.name.capitalize()
        return f"{name_cap}: {self.height}cm, {self.age} days old"


plant1: Plant = Plant('rose', 25, 30)
print("=== Day 1 ===")
print(plant1.get_info())
i = 0
while i < 6:
    plant1.grow(1)
    plant1.age_plant()
    i += 1

print("=== Day 7 ===")
print(plant1.get_info())
print(f"Growth this week: +{plant1.height - plant1.initial_height}cm")
