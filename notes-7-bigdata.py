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
    # Read the file
    header_row = file.readline()

    # Get information about the favorite pizza in SFU
    # Print the rest of the file
    for line in file:
        # fave pizza is column 4
        # a line is a string
        # convert the string to a list
        # split the line into columns
        columns = line.split(",")
        # get the favorite pizza
        favorite_pizza = columns[4]
        name = columns[1]
        # print the favorite pizza
        print(f"{name}'s favorite pizza is {favorite_pizza}")

    file.close()
    pass


if __name__ == "__main__":
    main()
