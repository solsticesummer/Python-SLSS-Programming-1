# Big data
# Author: Henry
# 17 November 2025

# Open files using Python
# Read the data in the files
# Interpret the data that we read


def main():
    # Get the file
    path = "data/sfu_best_cmpt120.csv"
    file = open(path)
    # # Read the file

    # # Get information about the favorite pizza in SFU
    # uncle_fatih = 0
    # club_ilia = 0
    # pizza_hut = 0

    # # Print the rest of the file
    # for line in file:
    #     # fave pizza is column 4
    #     # a line is a string
    #     # convert the string to a list
    #     # split the line into columns
    #     columns = line.split(",")
    #     # get the favorite pizza
    #     favorite_pizza = columns[4]

    #     # print the name and favorite pizza
    #     if favorite_pizza == "Uncle Fatih's":
    #         uncle_fatih += 1
    #     elif favorite_pizza == "Club Ilia":
    #         club_ilia += 1
    #     elif favorite_pizza == "Pizza Hut":
    #         pizza_hut += 1

    # # Dispaly results
    # print(f"Uncle Fatih's votes: {uncle_fatih}")
    # print(f"Club Ilia votes: {club_ilia}")
    # print(f"Pizza Hut votes : {pizza_hut}")

    # file.close()
    # pass
    # Read the data
    quesada = 0
    guadalupe = 0
    for line in file:
        columns = line.split(",")
        fav_burrito = columns[5]
        if fav_burrito == "Quesada (Cornerstone)":
            quesada += 1
        elif fav_burrito == "Guadalupe (MBC)":
            guadalupe += 1

    print(f"Quesada votes: {quesada}")
    print(f"Guadalupe votes: {guadalupe}")
    file.close()


if __name__ == "__main__":
    main()
