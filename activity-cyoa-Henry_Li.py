import time

greeting = "What's up"
print(greeting)
time.sleep(1)

health = 100
knowledge = 25
friends = 0
username = input("What is your username?")

print(f"It's nice to meet you {username}")
time.sleep(1)
print("You live in Neocity, a metropolis living in the future.")
time.sleep(2)
print(
    "However, in this future, mega corporations have obtained a monopoly over society's resources"
)
time.sleep(2)
print("You and many people are discontent with this situation")
time.sleep(2)
print("One day, you recieved a message")
time.sleep(2)
print("The message says: head towards the central tower")
time.sleep(2)
print("Are you gonna head there?")
time.sleep(2)

open = input("yes or no?")
if open == "yes":
    knowledge = 50
    print("You have a inkling this might link to a certain group")
    time.sleep(2)
    print("So you head towards the central tower")
    time.sleep(2)
    print(
        "Once you reach the central tower, you see a guard in front of the main entrance"
    )
    time.sleep(2)
    print("Do you try to sneak past him, approach him or leave?")
    choice = input("choice 1 or 2, or 3?")
    if choice == "1":
        health = 0
        print("You really thought you could sneak past a guard in the open?")
        time.sleep(1)
        print("The guard caught you and you got put in prison")
        time.sleep(2)
        print(
            "After thorough explaination, the guard decided to let you go, and you went back to repeating your mundane tasks"
        )
        time.sleep(2)
    elif choice == "2":
        friends = 1
        knowledge = 100
        print("You approach the guard and told him you have recieved a message")
        time.sleep(1)
        print("The guard takes a look at your message and lets you in")
        time.sleep(1)
        print(
            "You follow the guard and you go into a secret tunnel hidden inside the tower"
        )
        time.sleep(2)
        print("At the end of the tunnel, you see a familiar face")
        time.sleep(2)
        print("Henry, your old friend that dissapeared")
        time.sleep(2)
        print(
            "Turns out, you were living in an experimental civilazation and you have passed the experiment, allowing you to return to the real world"
        )
        time.sleep(2)
    elif choice == "3":
        knowledge = 0
        print("You gave up on your mission")
        time.sleep(2)
elif open == "no":
    knowledge = 0
    print("You left the message, thinking it was unsignificant")
    print("Little did you know how wrong you were")
    print("You continued living your boring life in the Neocity")
    print(
        "Sometimes, you would think about what if you opened that message and regret not being more curious"
    )
    print("But you will never know")

else:
    print("Invalid syntax")
    print("Start Over")

if friends > 1 and knowledge > 50 and health > 50:
    print("Good Job")
    time.sleep(1)
    print("You have completed the mission")
    time.sleep(1)
    print("GAME OVER")
else:
    print("You never find the truth")
    time.sleep(1)
    print("You failed the mission")
    time.sleep(1)
    print("GAME OVER")
