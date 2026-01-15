class SecurePlant:
    """Protect plant data with validation helpers."""

    def __init__(self, name: str) -> None:
        """Initialize secure plant with default protected attributes."""
        self.name = name.capitalize()
        self._height = 0     # prefix for private / protected
        self._age = 0        # prefix for private / protected

    def set_height(self, value: int) -> None:
        """Safely update height when non-negative."""
        if value >= 0:
            self._height = value
            print(f"Height updated: {value}cm [OK]")
        else:
            print(
                f"\nInvalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected\n")

    def set_age(self, value: int) -> None:
        """Safely update age when non-negative."""
        if value >= 0:
            self._age = value
            print(f"Age updated: {value} days [OK]")
        else:
            print(
                f"\nInvalid operation attempted: Age {value} days [REJECTED]")
            print("Security: Negative age rejected\n")

    def get_height(self) -> int:
        """Return current plant height."""
        return self._height

    def get_age(self) -> int:
        """Return current plant age."""
        return self._age


if __name__ == "__main__":
    plant: SecurePlant = SecurePlant('rose')
    print("=== Garden Security System ===")
    print("Plant created:", plant.name)
    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-5)
    current_height = plant.get_height()
    current_age = plant.get_age()
    print(
        f"Current plant: {plant.name} "
        f"({current_height}cm, {current_age} days)"
    )
