class GardenError(Exception):
    pass


class InvalidName(GardenError):
    pass


class WaterLevelError(GardenError):
    pass


class SunlightHoursError(GardenError):
    pass


class Plant:
    def __init__(self, plant_name: str, water_level: int,
                 sunlight_hours: int) -> None:
        self.plant_name = plant_name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


class GardenManager:
    def __init__(self, water_in_tank: int = 0) -> None:
        self.water_in_tank = water_in_tank

    plants = []

    @classmethod
    def add_plant(cls, plant: Plant) -> None:
        try:
            if not plant.plant_name:
                raise InvalidName("Plant name cannot be empty!")
        except InvalidName as e:
            print("Error adding plant:", e)
        else:
            cls.plants.append(plant)
            print(f"Added {plant.plant_name} successfully")

    @classmethod
    def water_plants(cls) -> None:
        print("Opening watering system")
        try:
            for plant in cls.plants:
                if not plant.plant_name:
                    raise TypeError(
                        f"Cannot water {plant.plant_name} - invalid plant!")
                else:
                    print(f"Watering {plant.plant_name} - success")
                    plant.water_level += 1
        except TypeError as e:
            print("Error watering plant:", e)
        finally:
            print("Cleaning watering system (cleanup)")

    @classmethod
    def check_health(cls) -> None:
        print("\nChecking plant health...")
        for plant in cls.plants:
            try:
                if plant.water_level > 10:
                    raise WaterLevelError(
                        f"Water level {plant.water_level} is too high "
                        f"(max 10)")
                elif plant.water_level < 1:
                    raise WaterLevelError(
                        f"Water level {plant.water_level} is too low "
                        f"(min 1)")
                elif plant.sunlight_hours < 2:
                    raise SunlightHoursError(
                        f"Sunlight hours {plant.sunlight_hours} is too low "
                        f"(min 2)")
                elif plant.sunlight_hours > 12:
                    raise SunlightHoursError(
                        f"Sunlight hours {plant.sunlight_hours} is too high "
                        f"(max 12)")
            except (WaterLevelError, SunlightHoursError) as e:
                print(f"Error checking {plant.plant_name}: {e}")
            else:
                print(
                    f"{plant.plant_name}: healthy (water: {plant.water_level},"
                    f" sun: {plant.sunlight_hours})")

    def error_recovery(self):
        try:
            if self.water_in_tank < 25:
                raise GardenError("Not enough water in tank")
            else:
                print("Water tank check - success")
        except GardenError as e:
            print("Caught GardenError:", e)
        finally:
            print("System recovered and continuing...")


garden1 = GardenManager(24)

tomato = Plant('tomato', 4, 8)
lettuce = Plant('lettuce', 14, 10)
test_plant = Plant('', 1, 2)

print("=== Garden Management System ===\n")
print("Adding plants to garden...")
garden1.add_plant(tomato)
garden1.add_plant(lettuce)
garden1.add_plant(test_plant)
print("\nWatering plants...")
garden1.water_plants()
print("\nChecking plant health...")
garden1.check_health()
print("\nTesting error recovery...")
garden1.error_recovery()
print("\nGarden management system test complete!")
