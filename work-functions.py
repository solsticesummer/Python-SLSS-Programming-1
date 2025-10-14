# Work - Functions
# Author - Henry
# Ocotober 14


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
