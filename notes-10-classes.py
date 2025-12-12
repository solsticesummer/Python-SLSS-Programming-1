# Classes and Objects
# Author: Henry
# 11 December 2025

import random


class Pokemon:
    def __init__(self):
        # Initialize the properties of Pokemon
        self.name = "Pikachu"
        self.type = "Electric"
        self.shiny = False
        self.age = 0
        self.level = 1
        print(f"Pokemon {self.name} is born!")
        # One out of 4096 is shiny
        if random.randint(0, 4095):
            self.shiny = False
        else:
            self.shiny = True
            print(f"{self.name} is shiny!")


if __name__ == "__main__":
    # Create a pokemon object
    pokemon1 = Pokemon()
    # View its properties
    print("Pokemon Name:", pokemon1.name)
    # Change some properties
    pokemon1.name = "Charizard"
    print("Pokemon Name:", pokemon1.name)
    # Create another pokemon object
    pokemon2 = Pokemon()
    print("Pokemon Name:", pokemon2.name)
    # Compare the two objects
    if pokemon1 == pokemon2:
        print("The two pokemons are the same.")
    else:
        print("The two pokemons are different.")
