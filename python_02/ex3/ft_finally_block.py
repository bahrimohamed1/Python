def water_plants(plant_list: list) -> None:
    """Waters plants with finally block for cleanup."""
    print("Opening watering system")
    try:
        for plant in plant_list:
            print("Watering " + plant)
    except TypeError:
        print(f"Error: Cannot water {plant} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """Tests watering system with finally block."""
    print("Testing normal watering...")
    plants = [
        'tomato',
        'lettuce',
        'carrots',
    ]
    water_plants(plants)
    print("Watering completed successfully!")
    print("\nTesting with error...")
    bad_plants = [
        'tomato',
        True,
        'lettuce',
        'carrots'
    ]
    water_plants(bad_plants)
    print("\nCleanup always happens, even with errors!")


print("=== Garden Watering System ===\n")
test_watering_system()
