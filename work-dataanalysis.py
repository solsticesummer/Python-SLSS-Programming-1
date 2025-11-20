# Data Analysis
# Author: Henry
# Nov 20 2025

# Analyse the data provided in class


def main():
    # do your work in here
    # or create a new function and call it in here
    path = "data/NYC_Central_Park_weather_1869-2022.csv"
    file = open(path)

    def data_points():
        total = 0
        for line in file:
            total += 1
        print(total)

    def avg():
        total = data_points()
        for line in file:
            columns = line.split(",")
            precpitation = float(columns[1])
            snowfall = float(columns[2])
            avg_rainfall = precpitation + snowfall) / total

        print(f"Average Rainfall: {avg_rainfall} inches")

    data_points()
    file.close()
    pass


if __name__ == "__main__":
    main()
