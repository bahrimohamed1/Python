"""Garden analytics platform demo for exercise 6."""


class Plant:
    """Base plant with common attributes."""

    def __init__(self, name: str, height: int) -> None:
        """Initialize a plant with its name and height in centimeters."""
        self.name = name
        self.height = height


class FloweringPlant(Plant):
    """Plant that can bloom."""

    def __init__(self, name: str, height: int, color: str) -> None:
        """Initialize a flowering plant with a bloom color."""
        super().__init__(name, height)
        self.color = color
        self.blooming = True


class PrizeFlower(FloweringPlant):
    """Special flowering plant with prize points."""

    def __init__(self, name: str, height: int, color: str, prize_points: int):
        """Initialize a prize flower with its score value."""
        super().__init__(name, height, color)
        self.prize_points = prize_points


class GardenManager:
    """Manage multiple gardens and provide analytics."""

    class GardenStats:
        """Helper for computing statistics about plants."""

        @staticmethod
        def total_height(plants: list[Plant]) -> int:
            """Return the total height of all plants."""
            return sum(plant.height for plant in plants)

        @staticmethod
        def count_types(plants: list[Plant]) -> tuple[int, int, int]:
            """Return counts of (plants, flowering, prize flowers)."""
            flowering = sum(isinstance(p, FloweringPlant) for p in plants)
            prize = sum(isinstance(p, PrizeFlower) for p in plants)
            return len(plants), flowering, prize

    def __init__(self, owner: str) -> None:
        """Create a manager for a specific owner's garden."""
        self.owner = owner
        self.plants: list[Plant] = []

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the garden if height is valid."""
        if self.validate_height(plant.height):
            self.plants.append(plant)
            print(f"Added {plant.name} to {self.owner}'s garden")
        else:
            print(f"Rejected {plant.name}: invalid height")

    def grow_all(self, amount: int) -> None:
        """Grow every plant by the given amount of centimeters."""
        for plant in self.plants:
            plant.height += amount
            print(f"{plant.name} grew {amount}cm")

    def report(self) -> None:
        """Print a simple report using the nested stats helper."""
        total, flowering, prize = self.GardenStats.count_types(self.plants)
        height_sum = self.GardenStats.total_height(self.plants)
        print(f"=== {self.owner}'s Garden Report ===")
        for plant in self.plants:
            extra = ""
            if isinstance(plant, PrizeFlower):
                extra = f", prize points: {plant.prize_points}"
            elif isinstance(plant, FloweringPlant):
                extra = f", color: {plant.color}"
            print(f"- {plant.name}: {plant.height}cm{extra}")
        print(
            f"Plants added: {total}, total height: {height_sum}cm, "
            f"flowering: {flowering}, prize flowers: {prize}"
        )

    @staticmethod
    def validate_height(height: int) -> bool:
        """Utility validation that does not depend on instance data."""
        return height >= 0

    @classmethod
    def create_garden_network(cls, owners: list[str]) -> list["GardenManager"]:
        """Create managers for all provided owners."""
        return [cls(owner) for owner in owners]


if __name__ == "__main__":
    managers = GardenManager.create_garden_network(["Alice", "Bob"])
    alice_garden = managers[0]

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    print("Alice is helping all plants grow...")
    alice_garden.grow_all(1)
    alice_garden.report()

    print("Height validation test:", GardenManager.validate_height(10))
    print("Total gardens managed:", len(managers))
