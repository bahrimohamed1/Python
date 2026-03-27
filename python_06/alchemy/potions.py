from .elements import create_water, create_earth, create_fire

water_result = create_water()
fire_result = create_fire()
earth_result = create_earth()

def healing_potion():
    return f"Healing potion brewed with {fire_result} and {water_result}"


def strength_potion():
    return f"Strength potion brewed with {earth_result} and {fire_result}"


def invisibility_potion():
    pass


def wisdom_potion():
    pass
