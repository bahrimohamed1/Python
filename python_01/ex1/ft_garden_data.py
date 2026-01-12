#!/usr/bin/python3.10

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        
def ft_garden_data():
    plant1 = Plant('Rose', 25, 30)
    plant2 = Plant('Sunflower', 80, 45)
    plant3 = Plant('Cactus', 15, 120)
    print(f"""=== Garden Plant Registry ===
{plant1.name.capitalize()}: {plant1.height}cm, {plant1.age} days old
{plant2.name.capitalize()}: {plant2.height}cm, {plant2.age} days old
{plant3.name.capitalize()}: {plant3.height}cm, {plant3.age} days old""")
    
    
if __name__ == '__main__':
    ft_garden_data()