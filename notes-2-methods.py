# Methods
# Author: Henry
# October 6

# ASk the user what the weather is like

weather = input("What's the weather like right now?")

if weather.lower().strip("!") == "rainy":
    print("You should bring an umbrella.")
elif weather.lower().strip(".!").strip() == "sunny":
    print("You should bring sunscreen.")
else:
    print("I see...")
