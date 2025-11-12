# Work - McDoBot
# Author - Henry
# October 6

# Write a McDonald's bot that asks if you want fries with your meal.
# Call it  work-mcdobot.py.
# It should accept  Yes/yes  or  No/no  as inputs, and
# reply appropriately depending on the answer.
# If the user inputs anything else, it should repeat back their answer
# and say that it does not understand.

meal = input("Would you like fries with your meal? (Yes/No)")

if meal.lower().strip("!.").strip() == "yes":
    print("Here's your meal with fries!")
elif meal.lower().strip("!.").strip() == "no":
    print("Here's your meal without fries!")
else:
    print("I dont understand. Please respond with yes or no.")
