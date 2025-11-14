# Math problems
# Author: Henry
# Nov 14 2025


def age_in_2049():
    current_age = int(input("What is your current age?"))
    print(f"In 2049 you will be {current_age + 24} years old!")


def olympic_judging():
    print("What score will you give out of 10?")
    score1 = float(input("Judge 1: "))
    if score1 > 10 or score1 < 0:
        print("please enter a valid number")
        return
    score2 = float(input("Judge 2: "))
    if score2 > 10 or score2 < 0:
        print("please enter a valid number")
        return
    score3 = float(input("Judge 3: "))
    if score3 > 10 or score3 < 0:
        print("please enter a valid number")
        return
    score4 = float(input("Judge 4: "))
    if score4 > 10 or score4 < 0:
        print("please enter a valid number")
        return
    score5 = float(input("Judge 5: "))
    if score5 > 10 or score5 < 0:
        print("please enter a valid number")
        return
    average = (score1 + score2 + score3 + score4 + score5) / 5
    print(f"Your olympic score is {average}.")


def mcdonalds():
    total = 0
    print("Would you like a burger for $5? (Yes/No)")
    answer1 = input().lower().strip(" ?!.,")
    if answer1 == "yes":
        total += 5
    elif answer1 == "no":
        total += 0
    else:
        print("Invalid response")
        return
    print("Would you like fries for $3? (Yes/No)")
    answer2 = input().lower().strip(" ?!.,")
    if answer2 == "yes":
        total += 3
    elif answer2 == "no":
        total += 0
    else:
        print("Invalid response, please try again.")
        return
    final_total = total * 1.14
    print(f"Your total is ${final_total}.")


age_in_2049()
mcdonalds()
olympic_judging()
