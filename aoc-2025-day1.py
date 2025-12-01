# AOC Day 1
# Author: Henry
# 1 December


def part1():
    with open("data/aoc-2025-day1.txt") as f:
        password = 0
        dial = 50
        for line in f:
            direction = line[0]
            distance = int(line[1:])
            if distance > 100:
                distance = int(line[2:])
            if direction == "R":
                dial += distance

            else:
                dial -= distance

            if dial > 99:
                dial -= 100
            if dial < 0:
                dial += 100

            if dial == 0 or dial == 100:
                password += 1
        print(password)


def part2():
    pass


if __name__ == "__main__":
    part1()
