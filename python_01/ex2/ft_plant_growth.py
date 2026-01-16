class Plant:
    """A class representing a plant with growth and aging capabilities."""
    
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a Plant instance.
        
        Args:
            name (str): The name of the plant.
            height (int): The initial height of the plant in centimeters.
            age (int): The age of the plant in days.
        """
        self.name = name
        self.height = height
        self.age = age
        self.initial_height = height

    def grow(self, amount: int) -> None:
        """Increase the plant's height by a specified amount.
        
        Args:
            amount (int): The amount to increase the plant's height in centimeters.
        """
        self.height += amount

    def age_plant(self) -> None:
        """Increase the plant's age by one day."""
        self.age += 1

    def get_info(self) -> str:
        """Get formatted information about the plant.
        
        Returns:
            str: A string containing the plant's name, height, and age.
        """
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
