# def main():
#     # Get the file
#     path = "data/sfu_best_cmpt120.csv"
#     file = open(path)
#     # Read the data
#     quesada = 0
#     guadalupe = 0
#     for line in file:
#         columns = line.split(",")
#         fav_burrito = columns[5]
#         if fav_burrito == "Quesada (Cornerstone)":
#             quesada += 1
#         elif fav_burrito == "Guadalupe (MBC)":
#             guadalupe += 1

#     print(f"Quesada votes: {quesada}")
#     print(f"Guadalupe votes: {guadalupe}")
#     file.close()
#     pass


# if __name__ == "__main__":
#     main()


def main():
    path = "data/sfu_best_cmpt120.csv"
    file = open(path)
    subway = 0
    steves_poke_bar = 0
    veggie_lunch = 0
    chopped_leaf = 0
    natures_garden = 0
    for line in file:
        columns = line.split(",")
        fav_healthy_food = columns[-1].lower().strip("\n")
        if fav_healthy_food == "subway":
            subway += 1
        elif fav_healthy_food == "steve's poke bar":
            steves_poke_bar += 1
        elif fav_healthy_food == "veggie lunch":
            veggie_lunch += 1
        elif fav_healthy_food == "chopped leaf":
            chopped_leaf += 1
        elif fav_healthy_food == "nature's garden":
            natures_garden += 1

    print(f"Subway votes: {subway}")
    print(f"Steve's Poke Bar votes: {steves_poke_bar}")
    print(f"Veggie Lunch votes: {veggie_lunch}")
    print(f"Chopped Leaf votes: {chopped_leaf}")
    print(f"Nature's Garden votes: {natures_garden}")
    file.close()
    pass


if __name__ == "__main__":
    main()
