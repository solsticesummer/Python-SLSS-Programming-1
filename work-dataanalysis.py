# Data Analysis
# Author: Henry
# Nov 20 2025

# Analyse the data provided in class


def main():
    # do your work in here
    # or create a new function and call it in here
    path = "data/NYC_Central_Park_weather_1869-2022.csv"
    file = open(path)

    def avg():
        file.readline()
        total = 0
        total_rainfall = 0
        total_min_temp = 0
        total_max_temp = 0
        total_june = 0
        for line in file:
            columns = line.strip("\n").split(",")
            date = columns[0]
            row = date.split("-")
            month = row[1]
            precpitation = float(columns[1]) if columns[1] != "" else 0
            min_temp = float(columns[4]) if columns[4] != "" else 0
            rainfall = precpitation

            total_rainfall += rainfall
            total += 1
            total_min_temp += min_temp

            if month == "06":
                max_temp = float(columns[5]) if columns[5] != "" else 0
                total_max_temp += max_temp
                total_june += 1
        avg_rainfall = total_rainfall / total
        avg_min_temp = total_min_temp / total
        avg_max_temp = total_max_temp / total_june

        print(total)
        print(avg_rainfall)
        print(avg_min_temp)
        avg_min_temp_celsius = (avg_min_temp - 32) * 5 / 9
        print(avg_min_temp_celsius)
        print(avg_max_temp)

    avg()

    file.close()
    pass


if __name__ == "__main__":
    main()
