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

    # Read the ret of the file
    for line in file:
        print(line)

    file.close()
    pass


if __name__ == "__main__":
    main()
