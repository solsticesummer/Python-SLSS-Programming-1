# Numbers and Operations
# Author: Henry
# Date: 2025-11-05

# Work with numbers and operations

# Create an algorithm to gather data to find the most popular bubble tea place around us

import os

NUM_VOTERS = 5


# Version 1
def vote_list_choices():
    """Display all the choices, 5 users votes for their choice, results will be printed"""

    CHOICES = [
        "A. Blenz",
        "B. Bubble Queen",
        "C. Sun Tea",
        "D. Heytea",
        "E. CoCo",
        "F. Fresh T",
    ]

    # buckets to hold all votes
    blenz = 0
    bubble_queen = 0
    sun_tea = 0
    heytea = 0
    coco = 0
    fresh_t = 0
    spoiled_votes = 0

    for _ in range(NUM_VOTERS):
        # Clear screen
        os.system("clear")

        # Show all the choices
        print("Vote for your favorite from the list")
        print("Give the letter of your choice")
        for choice in CHOICES:
            print(choice)

        # Ask the user for their choice
        vote = input("Enter your choice: ").strip(".,?! ").lower()

        # Keep track of a tally
        if vote == "a":
            blenz += 1
        elif vote == "b":
            bubble_queen += 1
        elif vote == "c":
            sun_tea += 1
        elif vote == "d":
            heytea += 1
        elif vote == "e":
            coco += 1
        elif vote == "f":
            fresh_t += 1
        else:
            spoiled_votes += 1

    # Data analysis
    # Give raw scores
    print("Voting results ---")
    print(f"Blenz: {blenz} votes")
    print(f"Bubble Queen: {bubble_queen} votes")
    print(f"Sun Tea: {sun_tea} votes")
    print(f"Heytea: {heytea} votes")
    print(f"CoCo: {coco} votes")
    print(f"Fresh T: {fresh_t} votes")
    print(f"Spoiled Votes: {spoiled_votes} votes")

    # Give scores as a percentage
    print("Vote share percentage ---")
    total = blenz + bubble_queen + sun_tea + heytea + coco + fresh_t + spoiled_votes
    print(f"Blenz: {blenz / total * 100} %")
    print(f"Bubble Queen: {bubble_queen / total * 100} %")
    print(f"Sun Tea: {sun_tea / total * 100} %")
    print(f"Heytea: {heytea / total * 100} %")
    print(f"CoCo: {coco / total * 100} %")
    print(f"Fresh T: {fresh_t / total * 100} %")
    print(f"Spoiled Votes: {spoiled_votes / total * 100} %")


# Version 2
# Ask the user to give their favorite bubble tea place
# Keep track of a tally
# Data analysis
# Give raw scores
# Give scores as a percentage


def chip_rater():
    # Help gather data about chip cripness and quality.
    questions = [
        "How crispy is the chip out of 5? 0 is mushy and 5 is super crisp.",
        "How would you rate the taste out of 5? 0 is unpalateble and 5 is gourmet.",
        "How fresh would you rate the chip out of 5? 0 is stale and 5 is pristine.",
    ]

    # Bucket to hold the total ratings
    total_ratings = 0

    # Give the test subject instructions
    print("Take one chip from the bag.")
    print("Eat it mindfully.")
    print("Give your rating.")

    # Ask questions to the subject
    for question in questions:
        # for each question
        print(question)

        # get their rating for that question out of 5
        rating = int(input().strip(" .,!?"))

        total_ratings += rating
    # print out the average rating out of 5
    average = total_ratings / len(questions)
    print(f"The average rating is {average} stars!")


def main():
    # vote_list_choices()
    chip_rater()


if __name__ == "__main__":
    main()
