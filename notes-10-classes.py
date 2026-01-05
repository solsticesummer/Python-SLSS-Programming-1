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
        self.age = 0
        self.level = 1
        self.health = 100
        # One out of 4096 is shiny
        if random.randint(0, 4095):
            self.shiny = False
        else:
            self.shiny = True
            print(f"{self.name} is shiny!")

        print("A Pokemon is born!")

    def super_effective(self):
        print(f"{self.name} is super effective!")

    def talk(self):
        """Hear what the pokemon has to say
        The pokemon says its species name."""
        print(f'{self.name} says, "{self.species}!".')

    def stats(self):
        print(f"----{self.name}------")
        print(f"    Name: {self.name}")
        print(f"    Species: {self.species}")
        print(f"    Type: {self.type}")
        print(f"    Shiny: {self.shiny}")
        print(f"    Age: {self.age}")
        print(f"    Level: {self.level}")
        print(f"    Health: {self.health}")
        print("--------------------")

    def dance(self):
        print(f"{self.name} moves to the left!")
        print(f"{self.name} moves to the right!")
        print(f"{self.name} spins around!")
        print(f"{self.name} jumps!")
        print(f"{self.name} dances!")

    def find_something(self, how_many_things=1) -> list[str]:
        """Send pokemon to find something

        Returns:
            a str representing what it found"""
        things = [
            "pinap berry",
            "razz berry",
            "nanab berry",
            "golden razz berry",
            "leftovers",
            "moon stone",
        ]
        found_things = []

        for _ in range(how_many_things):
            found_things.append(random.choice(things))

        return found_things


class squirtle(Pokemon):
    def __init__(self):
        super().__init__()
        self.name = "Squirtle"
        self.species = "Squirtle"
        self.type = "Water"
        self.age = 10
        self.level = 1

    def water_gun(self):
        """Shoots a water gun"""
        print(f"{self.name} shoots a water gun!")
        # TODO: check to see if its effective

    def bubble(self):
        """Creates a bubble"""
        print(f"{self.name} shoots a bubble!")
        # TODO: check to see if its effective


class charizard(Pokemon):
    def __init__(self):
        super().__init__()
        self.name = "Charizard"
        self.species = "Char"
        self.type = "Fire"
        self.age = 1000
        self.level = 100

    def flamethrower(self):
        print(f"{self.name} shoots a flamethrower!")

    def fire_blast(self):
        print(f"{self.name} uses fire blast!")


class mew(Pokemon):
    def __init__(self):
        super().__init__()
        self.name = "Mew"
        self.species = "Mew"
        self.type = "Psychic"
        self.age = 0
        self.level = 1


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
    # Check if both objects are pokemon
    if type(pokemon1) is Pokemon:
        print(f"{pokemon1.name} is a Pokemon.")
    if type(pokemon2) is Pokemon:
        print(f"{pokemon2.name} is a Pokemon.")

    # Squirtle
    squirtle1 = squirtle()
    squirtle1.stats()
    squirtle1.talk()
    squirtle1.water_gun()
    squirtle1.super_effective()
    squirtle1.bubble()
    squirtle1.super_effective()

    # Charizard
    charizard1 = charizard()
    charizard1.stats()
    charizard1.talk()
    charizard1.fire_blast()
    charizard1.flamethrower()

    # Mew
    mew1 = mew()
    mew1.stats()
    mew1.talk()
