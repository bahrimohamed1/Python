class InvalidName(Exception):
    pass


def water_plants(plant_list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if not isinstance(plant, str):
                raise InvalidName(f"Cannot water {plant} - invalid plant!")
            else:
                print("Watering", plant)
    except InvalidName as e:
        print("Error:", e)
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("Testing normal watering...")
    plants = [
        'tomato',
        'lettuce',
        'carrots',
    ]
    water_plants(plants)
    print("Watering completed succefully!")
    print("\nTesting with error...")
    plants = [
        'tomato',
        None,
        'lettuce',
        'carrots'
    ]
    water_plants(plants)
    print("\nCleanup always happens, even with errors!")


print("=== Garden Watering System ===\n")
test_watering_system()
