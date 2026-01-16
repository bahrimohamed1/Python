class Plant:
    """A class representing a plant with basic attributes."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a Plant instance.

        Args:
            name (str): The name of the plant.
            height (int): The height of the plant in centimeters.
            age (int): The age of the plant in days.
        """
        self.name = name
        self.height = height
        self.age = age


plants = [
    Plant("Rose", 25, 30),
    Plant("Oak", 200, 365),
    Plant("Cactus", 5, 90),
    Plant("Sunflower", 80, 45),
    Plant("Fern", 15, 120)
]


print("=== Plant Factory Output ===")
for plant in plants:
    name_cap = plant.name.capitalize()
    print(
        f"Created: {name_cap} ({plant.height}cm, {plant.age} days)")
print("\nTotal plants created:", len(plants))
