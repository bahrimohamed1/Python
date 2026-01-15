class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name.title()
        self.height = height

    def grow(self, value: int = 1) -> str:
        self.height += value
        return f"{self.name} grew {value}cm"


class Floweringplant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color.lower()
        self.bloom = True

    def bloom_status(self) -> str:
        return "blooming" if self.bloom else "not blooming"


class PrizeFlower(Floweringplant):
    def __init__(self, name: str, height: int, color: str, prize: int) -> None:
        super().__init__(name, height, color)
        self.prize = prize

    def get_prize(self) -> str:
        return f"Prize points: {self.prize}"


class GardenManager:

    def __init__(self, name: str) -> None:
        self.name = name.capitalize()
        self.plants = []
        self.stats = self.GardenStats(self.plants)
    
    def get_report(self) -> str:
        counts = self.stats.count_type()
        return (
            f"=== {self.name}'s Garden Report ===\n"
            f"Plants added: {self.stats.count_plants()}\n"
            f"Plant types: {counts['regular']} regular, "
            f"{counts['flowering']} flowering, "
            f"{counts['prize']} prize flowers"
        )
        
    def grow_all_plants(self) -> None:
        print(f"{self.name} is helping all plants grow")
        for plant in self.plants:
            print(plant.grow())
            
    @classmethod
    def create_garden_network(cls, names: list) -> list:
        """Class method - creates multiple gardens at once."""
        print(f"Creating garden network with {len(names)} gardens...")
        gardens = []
        for name in names:
            gardens.append(cls(name))
        return gardens

    def add_plant(self, plant: Plant) -> str:
        self.plants.append(plant)
        return f"Added {plant.name} to {self.name}'s garden"

    class GardenStats:
        def __init__(self, plants: list) -> None:
            self.plants = plants
            
        def count_plants(self) -> int:
            return len(self.plants)
        
        def count_type(self) -> dict:
            count = {"regular": 0, "flowering": 0, "prize": 0}
            for plant in self.plants:
                if isinstance(plant, PrizeFlower):
                    count["prize"] += 1
                if isinstance(plant, Floweringplant):
                    count["flowering"] += 1
                else :
                    count["regular"] += 1
            return count
        
        
        
        
        
    # @classmethod
    # def create_garden_network(cls) -> None:
    #     pass

    # @staticmethod
    # def validate_height(height: int) -> bool:
    #     return height >= 0


alice: GardenManager = GardenManager('alice')
bob: GardenManager = GardenManager("bob")
oak = Plant('oak tree', 100)
rose = Plant('Rose', 25)
sunflower = Plant('sunflower', 50)

print("=== Garden Management System Demo ===\n")

print(alice.add_plant(oak))
print(alice.add_plant(rose))
print(alice.add_plant(sunflower))

print(f"\n{alice.name} is helping all plants grow...")

print(oak.grow())
print(rose.grow())
print(sunflower.grow())
