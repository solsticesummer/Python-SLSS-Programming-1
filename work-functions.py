# Create a function that generates a message that changes based on a given "mood."
# Define a function called create_mood_message.
# It should accept two parameters: name and mood.
# Make the mood parameter optional by giving it a default value of "neutral".
# Inside the function, use an if/elif/else block to check the value of mood:
# If mood is "happy", return a cheerful message like f"Hey {name}, great to see you smiling!".
# If mood is "sad", return a supportive message like f"I hope your day gets better, {name}.".
# If mood  is "neutral", return a message like f"Sometimes you have average days, {name}." .
# For any other mood (the else case), return a neutral message like f"Hi {name}, hope you're having a good day.".


def create_mood_message(mood: str = "neutral"):
    name = input("What is your name?").strip("!. ").lower()
    mood = input("How are you feeling today? (happy/sad/neutral)").strip("!. ").lower()
    if mood == "happy":
        return f"Hey {name}, great to see you smiling!"
    elif mood == "sad":
        return f"I hope your day gets better, {name}."
    elif mood == "neutral":
        return f"Sometimes you have average days, {name}."
    else:
        return f"Hi {name}, hope you're having a good day."


print(create_mood_message())


def average():
    num_1 = 101
    num_2 = 91
    num_3 = 85
    totalspeed = num_1 + num_2 + num_3
    average = totalspeed / 3
    return average


print(average())
