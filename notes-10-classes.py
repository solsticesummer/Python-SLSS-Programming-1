# Classes and Objects
# Author: Henry
# 11 December 2025

import random


class Pokemon:
    def __init__(self):
        # Initialize the properties of Pokemon
        self.name = ""
        self.species = ""
        self.type = ""
        # One out of 4096 is shiny
        if random.randint(0, 4095):
            self.shiny = False
        else:
            self.shiny = True
            print(f"{self.name} is shiny!")

        print("A Pokemon is born!")

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
        print("--------------------")

    def dance(self):
        print(f"{self.name} moves to the left!")
        print(f"{self.name} moves to the right!")
        print(f"{self.name} spins around!")
        print(f"{self.name} jumps!")
        print(f"{self.name} dances!")


class squirtle(Pokemon):
    def __init__(self):
        super().__init__()
        self.name = "Squirtle"
        self.species = "Squirt"
        self.type = "Water"

    def water_gun(self):
        """Shoots a water gun"""
        print(f"{self.name} shoots a water gun!")
        # TODO: check to see if its effective


class charizard(Pokemon):
    def __init__(self):
        super().__init__()
        self.name = "Charizard"
        self.species = "Char"
        self.type = "Fire"

    def fireball(self):
        print(f"{self.name} shoots a fireball!")


if __name__ == "__main__":
    # Create a pokemon object
    pokemon1 = Pokemon()
    pokemon1.name = "Pikachu"
    # View its properties
    print("Pokemon Name:", pokemon1.name)
    # Change some properties
    pokemon1.shiny = True
    # Create another pokemon object
    pokemon2 = Pokemon()
    pokemon2.name = "Bulbasaur"
    pokemon2.shiny = False
    print("Pokemon Name:", pokemon2.name)
    # Compare the two objects
    if pokemon1 == pokemon2:
        print("The two pokemons are the same.")
    else:
        print("The two pokemons are different.")

    # Squirtle
    squirtle1 = squirtle()
    squirtle1.stats()
    squirtle1.talk()
    squirtle1.water_gun()

    # Charizard
    charizard1 = charizard()
    charizard1.name = "Charizard"
    charizard1.stats()
    charizard1.talk()
    charizard1.fireball()
