def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    try:
        if not plant_name:
            raise ValueError("Plant name cannot be empty!")
        elif water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")
        elif water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 1)")
        elif sunlight_hours > 12:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too high (max 12)")
        elif sunlight_hours < 2:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too low (min 2)")
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===")
    print("\nTesting good values")
    check_plant_health('tomato', 1, 2)
    print("\nTesting empty plant name")
    check_plant_health('', 1, 2)
    print("\nTesting bad water level...")
    check_plant_health('tomato', 15, 2)
    print("\nTesting bad sunlight hours...")
    check_plant_health('tomato', 1, 0)
    print("\nAll error raising tests completed!")


test_plant_checks()
