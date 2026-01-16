class SecurePlant:
    """A class representing a plant with secure attribute access.
    
    This class uses private attributes with validation to ensure
    that only valid values are set for height and age."""
    
    def __init__(self, name: str) -> None:
        """Initialize a SecurePlant instance.
        
        Args:
            name (str): The name of the plant (will be capitalized).
        """
        self.name = name.capitalize()
        self._height = 0     # prefix for private / protected
        self._age = 0        # prefix for private / protected

    def set_height(self, value: int) -> None:
        """Set the plant's height with validation.
        
        Args:
            value (int): The height value to set in centimeters.
                        Must be non-negative.
        """
        if value >= 0:
            self._height = value
            print(f"Height updated: {value}cm [OK]")
        else:
            print(
                f"\nInvalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected\n")

    def set_age(self, value: int) -> None:
        """Set the plant's age with validation.
        
        Args:
            value (int): The age value to set in days.
                        Must be non-negative.
        """
        if value >= 0:
            self._age = value
            print(f"Age updated: {value} days [OK]")
        else:
            print(
                f"\nInvalid operation attempted: Age {value} days [REJECTED]")
            print("Security: Negative age rejected\n")

    def get_height(self) -> int:
        """Get the plant's height.
        
        Returns:
            int: The height of the plant in centimeters.
        """
        return self._height

    def get_age(self) -> int:
        """Get the plant's age.
        
        Returns:
            int: The age of the plant in days.
        """
        return self._age


plant: SecurePlant = SecurePlant('rose')
print("=== Garden Security System ===")
print("Plant created:", plant.name)
plant.set_height(25)
plant.set_age(30)
plant.set_height(-5)
current_height = plant.get_height()
current_age = plant.get_age()
print(f"Current plant: {plant.name} ({current_height}cm, {current_age} days)")
