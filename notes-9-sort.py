# Intro to Sort
# Author: Henry
# 4 December

# import csv

# Sorting Algorithms
# The code below uses linear search to find songs from a particular artist
# We're going to sort the results using Selection Sort
#     * implement basic version
#     * implement sort with songs based on YouTube views in descending order


def selection_sort(li: list[int], ascending=True) -> list[int]:
    """Sorts a given list using selection sort

    Params:
        l - list of nums to be sorted
        ascending - True if order is ascending

    Returns:
        a sorted list"""

    num_items = len(li)

    if ascending:
        # start at the beginning of the list
        for i in range(num_items):
            lowest_num = li[i]
            lowest_index = i
            # check the rest of the list
            for j in range(i + 1, num_items):
                if li[j] < lowest_num:
                    lowest_num = li[j]
                    lowest_index = j

            # swap the current index with the lowest
            li[i], li[lowest_index] = li[lowest_index], li[i]
    else:
        # start at the beginning of the list
        for i in range(num_items):
            highest_num = li[i]
            highest_index = i
            # check the rest of the list
            for j in range(i + 1, num_items):
                if li[j] > highest_num:
                    highest_num = li[j]
                    highest_index = j

            # swap the current index with the highest
            li[i], li[highest_index] = li[highest_index], li[i]

    return li


if __name__ == "__main__":
    sorted_list = selection_sort([1, 43, 55, -11, 100, 34])

    print(sorted_list)
