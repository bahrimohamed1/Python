def display_plant_info():
    """Display information about a plant in the garden.
    
    This function prints formatted information about a Rose plant
    including its name, height in centimeters, and age in days.
    """
    name = "Rose"
    height = 25
    age = 30

    print(
        f"""=== Welcome to My Garden ===
Plant: {name}
Height: {height}cm
Age: {age} days\n
=== End of Program ===""")


if __name__ == '__main__':
    display_plant_info()
