class Plant:
    """Base plant class."""

    def __init__(self, name: str) -> None:
        """Initialize a plant with a name."""
        self.name = name.title()

    def grow(self) -> str:
        """Instance method to simulate plant growth."""
        return f"{self.name} is growing"


class FloweringPlant(Plant):
    """Plant that flowers, inherits from Plant."""

    def __init__(self, name: str, color: str) -> None:
        """Initialize a flowering plant with name and color."""
        super().__init__(name)
        self.color = color.lower()


class PrizeFlower(FloweringPlant):
    """Prize-winning flower, inherits from FloweringPlant."""

    def __init__(self, name: str, color: str, points: int) -> None:
        """Initialize a prize flower with name, color, and points."""
        super().__init__(name, color)
        self.points = points


class GardenManager:
    """Manages multiple gardens with a nested statistics helper."""

    @classmethod
    def create_garden_network(cls) -> str:
        """Class method to create a garden network."""
        return "Garden network created"

    @staticmethod
    def validate_height(height: int) -> bool:
        """Static method to validate plant height."""
        return height > 0

    def __init__(self) -> None:
        """Initialize a garden manager with empty gardens list."""
        self.plants = []

    def add_plant(self, plant: Plant) -> str:
        """Instance method to add a new garden."""
        self.plants.append(plant)
        return f"Added {plant.name}"

    class GardenStats:
        """Nested class for calculating garden statistics."""

        def display_stats(self, plants: list) -> str:
            """Instance method to display garden statistics."""
            if not plants:
                return "No plants in garden"
            plant_count = len(plants)
            flower_count = sum(
                1 for p in plants if isinstance(p, FloweringPlant))
            prize_count = sum(
                1 for p in plants if isinstance(p, PrizeFlower))
            return f"Plants: {plant_count}, Flowers: {flower_count}, Prize: {prize_count}"


def water_plant(plant: Plant):
    """Non-member utility function to water a plant."""
    return f"Watering {plant.name}"

manager = GardenManager()

print(manager.create_garden_network())

print(GardenManager.validate_height(10))

plant = Plant("Oak")
print(plant.grow())

print(manager.add_plant(plant))
print(manager.add_plant(FloweringPlant("Rose", "red")))
print(manager.add_plant(PrizeFlower("Sunflower", "yellow", 100)))

print(water_plant(plant))

stats = GardenManager.GardenStats()
print(stats.display_stats(manager.plants))