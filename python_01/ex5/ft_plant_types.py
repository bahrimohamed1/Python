class Plant:
    """Base class representing a plant with basic attributes."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a Plant instance.

        Args:
            name (str): The name of the plant (will be capitalized).
            height (int): The height of the plant in centimeters.
            age (int): The age of the plant in days.
        """
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def get_info(self) -> str:
        """Get formatted information about the plant.

        Returns:
            str: A string containing the plant's name, height, and age.
        """
        return f"\n{self.name}: {self.height}cm, {self.age} days"


class Flower(Plant):
    """A class representing a flowering plant.

    Inherits from Plant and adds color attribute and blooming capability."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initialize a Flower instance.

        Args:
            name (str): The name of the flower.
            height (int): The height of the flower in centimeters.
            age (int): The age of the flower in days.
            color (str): The color of the flower.
        """
        super().__init__(name, height, age)
        self.color = color.lower()

    def bloom(self) -> None:
        """Make the flower bloom and display a message."""
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> str:
        """Get formatted information about the flower.

        Returns:
            str: A string containing the flower's name, height, age, and color.
        """
        return f"\n{self.name} (Flower): {self.height}cm, " \
            f"{self.age} days, {self.color} color"


class Tree(Plant):
    """A class representing a tree.

    Inherits from Plant and adds trunk diameter and shade calculation."""

    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        """Initialize a Tree instance.

        Args:
            name (str): The name of the tree.
            height (int): The height of the tree in centimeters.
            age (int): The age of the tree in days.
            trunk_diameter (int): The diameter of the tree trunk.
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> int:
        """Calculate the shade area produced by the tree.

        Returns:
            int: The area of shade in square meters.
        """
        height_meters = self.height / 100
        area = 3.14 * (height_meters ** 2)
        return int(area)

    def get_info(self) -> str:
        """Get formatted information about the tree.

        Returns:
            str: A string containing the tree's name, height, age,
                 trunk diameter, and shade area.
        """
        area = self.produce_shade()
        return f"\n{self.name} (Tree): {self.height}cm, " \
            f"{self.age} days, {self.trunk_diameter}cm diameter\n" \
            f"{self.name} provides {area} square meters of shade"


class Vegetable(Plant):
    """A class representing a vegetable plant.

    Inherits from Plant and adds harvest season and nutritional information."""

    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        """Initialize a Vegetable instance.

        Args:
            name (str): The name of the vegetable.
            height (int): The height of the vegetable plant in centimeters.
            age (int): The age of the vegetable plant in days.
            harvest_season (str): The harvest season.
            nutritional_value (str): The primary vitamin.
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season.lower()
        self.nutritional_value = nutritional_value.upper()

    def get_info(self) -> str:
        """Get formatted information about the vegetable.

        Returns:
            str: A string containing the vegetable's name, height, age,
                 harvest season, and nutritional value.
        """
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
