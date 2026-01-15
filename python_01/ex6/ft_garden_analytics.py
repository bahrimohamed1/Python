class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name.title()
        self._height = height

    def grow(self) -> str:
        self._height += 1
        return f"{self.name} grew 1cm"

    def get_info(self) -> str:
        return f"- {self.name}: {self._height}cm"

    @staticmethod
    def validate_height(height: int) -> bool:
        return height > 0


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color

    def get_info(self) -> str:
        return f"{super().get_info()}, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, prize: int) -> None:
        super().__init__(name, height, color)
        self.prize = prize

    def get_info(self) -> str:
        return f"{super().get_info()}, Prize points: {self.prize}"


class GardenManager:
    count_managers = 0

    def __init__(self, name: str) -> None:
        self.name = name.capitalize()
        self.plants = []
        GardenManager.count_managers += 1

    def add_plant(self, plant: Plant) -> str:
        self.plants.append(plant)
        return f"Added {plant.name} to {self.name}'s garden"

    @classmethod
    def create_garden_network(cls) -> str:
        return f"=== Garden Network System Active ===\n" \
            f"=== Total managers: {cls.count_managers} ==="

    def grow_all(self) -> None:
        print(f"\n{self.name} is helping all plants grow...")
        for plant in self.plants:
            print(plant.grow())

    class GardenStats:
        def display_stats(self, plants: list) -> str:
            total_height = sum(plant._height for plant in plants)
            avg_height = int(total_height / len(plants))
            return ("No plants in garden" if not plants else
                    f"Total plants in garden: {len(plants)}\n"
                    f"Average height of plants: {avg_height}")


def water_plant(plant: Plant):
    """Non-member utility function to water a plant."""
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
