# Classes and Objects
# Author: Henry
# 11 December 2025

import random


class Pokemon:
    def __init__(self):
        # Initialize the properties of Pokemon
        self.name = "Pikachu"
        self.species = "Pikachu"
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

    def talk(self):
        """Hear what the pokemon has to say
        The pokemon says its species name."""
        print(f'{self.name} says, "{self.species}".')

    def stats(self):
        print(f"----{self.species}------")
        print(f"    Name: {self.name}")
        print(f"    Species: {self.species}")
        print(f"    Type: {self.type}")
        print(f"    Shiny: {self.shiny}")
        print(f"    Age: {self.age}")
        print(f"    Level: {self.level}")
        print("--------------------")

    def dance(self):
        print(f"{self.name} moves to the left!")
        print(f"{self.name} moves to the right!")
        print(f"{self.name} spins around!")
        print(f"{self.name} jumps!")
        print(f"{self.name} dances!")


class squirtle(Pokemon):
    def water_gun(self):
        """Shoots a water gun"""
        print(f"{self.name} shoots a water gun!")
        # TODO: check to see if its effective


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
    pokemon1.talk()
    pokemon2.talk()
    pokemon1.stats()
    pokemon2.stats()
    pokemon1.dance()
    pokemon2.dance()

    squirtle1 = squirtle()
    squirtle1.name = "Squirtle"
    squirtle1.talk()
    squirtle1.water_gun()
