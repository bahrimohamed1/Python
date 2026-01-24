class GardenError(Exception):
    @classmethod
    def raise_all_errors(cls) -> None:
        errors = cls.__subclasses__()
        for error in errors:
            try:
                raise error
            except error as e:
                print("Caught a garden error:", e)


class PlantError(GardenError):
    def __init__(self, name: str = 'tomato') -> None:
        super().__init__(f"The {name.capitalize()} plant is wilting!")


class WaterError(GardenError):
    def __init__(self) -> None:
        super().__init__("Not enough water in the tank!")


def garden_operations(option: str) -> None:
    if option == 'plant':
        try:
            raise PlantError("tomato")
        except PlantError as e:
            print("Caught PlantError:", e)
    elif option == 'water':
        try:
            raise WaterError()
        except WaterError as e:
            print("Caught WaterError:", e)
    elif option == 'all':
        try:
            GardenError.raise_all_errors()
        except WaterError as e:
            print(e)


def test_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    garden_operations('plant')

    print("\nTesting WaterError...")
    garden_operations('water')

    print("\nTesting catching all garden errors...")
    garden_operations('all')

    print("\nAll custom error types work correctly!")


test_errors()
