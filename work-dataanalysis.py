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

    def avg_rainfall():
        total = 0
        total_rainfall = 0

        for line in file:
            columns = line.split(",")
            precpitation = float(columns[1])
            snowfall = float(columns[2])
            rainfall = precpitation + snowfall
            total_rainfall += rainfall
            total += 1
        avg_rainfall = total_rainfall / total
        print(avg_rainfall)

    # data_points()
    avg_rainfall()

    file.close()
    pass


if __name__ == "__main__":
    main()
