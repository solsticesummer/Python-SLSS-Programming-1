def main():
    # Get the file
    path = "data/sfu_best_cmpt120.csv"
    file = open(path)
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
    pass


if __name__ == "__main__":
    main()
