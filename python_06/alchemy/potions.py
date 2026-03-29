from .elements import create_water, create_earth, create_fire, create_air

water_result = create_water()
fire_result = create_fire()
earth_result = create_earth()
air_result = create_air()


def healing_potion():
    water_result = create_water()
    fire_result = create_fire()
    return f"Healing potion brewed with {fire_result} and {water_result}"


def strength_potion():
    fire_result = create_fire()
    earth_result = create_earth()
    return f"Strength potion brewed with {earth_result} and {fire_result}"


def invisibility_potion():
    air_result = create_air()
    water_result = create_water()
    return f"Invisibility potion brewed with {air_result} and {water_result}"


def wisdom_potion():
    water_result = create_water()
    fire_result = create_fire()
    earth_result = create_earth()
    air_result = create_air()
    all_four_results = f"{water_result}, {fire_result}" +\
        f"{earth_result}, {air_result}"

    return f"Wisdom potion brewed with all elements: {all_four_results}"
