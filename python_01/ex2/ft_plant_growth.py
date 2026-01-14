class Plant:
    """Represent a plant that can grow over time."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize plant with its name, height (cm) and age (days)."""
        self.name = name
        self.height = height
        self.age = age
        self.initial_height = height

    def grow(self, amount: int) -> None:
        """Increase plant height by the given amount (cm)."""
        self.height += amount

    def age_plant(self) -> None:
        """Increase plant age by one day."""
        self.age += 1

    def get_info(self) -> str:
        """Return formatted information about the plant."""
        name_cap = self.name.capitalize()
        return f"{name_cap}: {self.height}cm, {self.age} days old"


if __name__ == "__main__":
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
