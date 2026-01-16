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


plant1: Plant = Plant('rose', 25, 30)
plant2: Plant = Plant('sunflower', 80, 45)
plant3: Plant = Plant('cactus', 15, 120)
print(f"""=== Garden Plant Registry ===
{plant1.name.capitalize()}: {plant1.height}cm, {plant1.age} days old
{plant2.name.capitalize()}: {plant2.height}cm, {plant2.age} days old
{plant3.name.capitalize()}: {plant3.height}cm, {plant3.age} days old""")
