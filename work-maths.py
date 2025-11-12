# Work - Maths
# Author - Henry
# November 12

import math


# Machines are good at crunching numbers - faster and more accurately than most humans!
# Create a small program that calculates something useful to you (making you smile is useful).
# It should take user input, at use at least one of the number operators we saw in class: + / * -.
# You may modify one of your previous exercises to include calculations, if you wish.
#
def program():
    print("I can help you find the square and square root of your number.")
    num = int(input("What is your number?  ").strip(" .?,!"))
    print(f"{math.sqrt(num)} is the square root of your number.")
    answer = num * num
    print(f"{answer} is the square of your number.")


def main():
    program()


if __name__ == "__main__":
    main()
