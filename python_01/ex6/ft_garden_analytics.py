class Plant:
    """Base class representing a plant with growth capability."""

    def __init__(self, name: str, height: int) -> None:
        """Initialize a Plant instance.

        Args:
            name (str): The name of the plant.
            height (int): The initial height of the plant in centimeters.
        """
        self.name = name.title()
        self._height = height

    def grow(self) -> str:
        """Increase the plant's height by 1 centimeter.

        Returns:
            str: A message indicating the plant grew.
        """
        self._height += 1
        return f"{self.name} grew 1cm"

    def get_info(self) -> str:
        """Get formatted information about the plant.

        Returns:
            str: A string containing the plant's name and height.
        """
        return f"- {self.name}: {self._height}cm"

    @staticmethod
    def validate_height(height: int) -> bool:
        """Validate that a height value is positive.

        Args:
            height (int): The height value to validate.

        Returns:
            bool: True if height is greater than 0, False otherwise.
        """
        return height > 0


class FloweringPlant(Plant):
    """A class representing a flowering plant.

    Inherits from Plant and adds color attribute."""

    def __init__(self, name: str, height: int, color: str) -> None:
        """Initialize a FloweringPlant instance.

        Args:
            name (str): The name of the flowering plant.
            height (int): The initial height of the plant in centimeters.
            color (str): The color of the flowers.
        """
        super().__init__(name, height)
        self.color = color

    def get_info(self) -> str:
        """Get formatted information about the flowering plant.

        Returns:
            str: A string containing the plant's name, height, color,
                and bloom status.
        """
        return f"{super().get_info()}, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    """A class representing a prize-winning flowering plant.

    Inherits from FloweringPlant and adds prize points."""

    def __init__(self, name: str, height: int, color: str, prize: int) -> None:
        """Initialize a PrizeFlower instance.

        Args:
            name (str): The name of the prize flower.
            height (int): The initial height of the plant in centimeters.
            color (str): The color of the flowers.
            prize (int): The number of prize points.
        """
        super().__init__(name, height, color)
        self.prize = prize

    def get_info(self) -> str:
        """Get formatted information about the prize flower.

        Returns:
            str: A string containing the plant's name, height, color,
                 bloom status, and prize points.
        """
        return f"{super().get_info()}, Prize points: {self.prize}"


class GardenManager:
    """A class for managing a garden of plants.

    This class tracks plants in a garden and provides management functionality
    including adding plants, growing all plants, and tracking statistics."""

    count_managers = 0

    def __init__(self, name: str) -> None:
        """Initialize a GardenManager instance.

        Args:
            name (str): The name of the garden manager (will be capitalized).
        """
        self.name = name.capitalize()
        self.plants = []
        GardenManager.count_managers += 1

    def add_plant(self, plant: Plant) -> str:
        """Add a plant to the manager's garden.

        Args:
            plant (Plant): The plant to add to the garden.

        Returns:
            str: A confirmation message indicating the plant was added.
        """
        self.plants.append(plant)
        return f"Added {plant.name} to {self.name}'s garden"

    @classmethod
    def create_garden_network(cls) -> str:
        """Create and display the garden network system information.

        Returns:
            str: A message showing the network status
                    and total number of managers.
        """
        return f"=== Garden Network System Active ===\n" \
            f"=== Total managers: {cls.count_managers} ==="

    def grow_all(self) -> None:
        """Help all plants in the garden grow by 1 centimeter each."""
        print(f"\n{self.name} is helping all plants grow...")
        for plant in self.plants:
            print(plant.grow())

    class GardenStats:
        """Nested class for calculating and displaying garden statistics.

        This class provides methods to analyze plants in a garden.
        """

        def display_stats(self, plants: list) -> str:
            """Calculate and display statistics for a list of plants.

            Args:
                plants (list): A list of Plant objects to analyze.

            Returns:
                str: A string containing total plant count and average height,
                     or a message if the garden is empty.
            """
            if not plants:
                return "No plants in garden"
            total_height = sum(plant._height for plant in plants)
            avg_height = int(total_height / len(plants))
            return (f"Total plants in garden: {len(plants)}\n"
                    f"Average height of plants: {avg_height}")


def water_plant(plant: Plant):
    """Non-member utility function to water a plant.

    Args:
        plant (Plant): The plant to be watered.

    Returns:
        str: A message indicating the plant is being watered.
    """
    return f"Watering {plant.name}"


oak = Plant('oak tree', 120)
rose = FloweringPlant('rose', 25, 'red')
sunflower = PrizeFlower('sunflower', 50, 'yellow', 10)

alice = GardenManager('alice')
bob = GardenManager('bob')

print(GardenManager.create_garden_network())
print(alice.add_plant(oak))
print(alice.add_plant(rose))
print(alice.add_plant(sunflower))

print(
    f"\nHeight validation ({oak._height}cm):"
    f"{Plant.validate_height(oak._height)}")

alice.grow_all()

print(f"\n=== {alice.name} Garden Report ===")
print("Plants in garden:")
print(oak.get_info())
print(rose.get_info())
print(sunflower.get_info())

print(f"\n{water_plant(rose)}")

stats = GardenManager.GardenStats()
print(f"\n{stats.display_stats(alice.plants)}")
