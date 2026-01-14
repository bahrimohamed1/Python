class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def get_info(self) -> str:
        return f"\n{self.name}: {self.height}cm, {self.age} days"


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color.lower()

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> str:
        return f"\n{self.name} (Flower): {self.height}cm, " \
            f"{self.age} days, {self.color} color"


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> int:
        height_meters = self.height / 100
        area = 3.14 * (height_meters ** 2)
        return int(area)

    def get_info(self) -> str:
        area = self.produce_shade()
        return f"\n{self.name} (Tree): {self.height}cm, " \
            f"{self.age} days, {self.trunk_diameter}cm diameter\n" \
            f"{self.name} provides {area} square meters of shade"


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season.lower()
        self.nutritional_value = nutritional_value.upper()

    def get_info(self) -> str:
        return f"\n{self.name} (Vegetable): {self.height}cm, " \
            f"{self.age} days, {self.harvest_season} harvest\n" \
            f"{self.name} is rich in vitamin {self.nutritional_value}"


sunflower: Flower = Flower('Sunflower', 30, 45, 'yellow')
rose: Flower = Flower('rose', 25, 30, 'red')
willow: Tree = Tree('willow', 120, 365, 15)
oak: Tree = Tree('Oak', 500, 1825, 50)
tomato: Vegetable = Vegetable('tomato', 80, 90, 'summer', 'c')
potato: Vegetable = Vegetable('Potato', 50, 150, 'winter', 'c')
print("=== Garden Plant Types ===")
print(rose.get_info())
rose.bloom()
print(sunflower.get_info())
sunflower.bloom()
print(oak.get_info())
print(willow.get_info())
print(tomato.get_info())
print(potato.get_info())
