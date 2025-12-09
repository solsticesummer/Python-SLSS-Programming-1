# Intro to Sort
# Author: Henry
# 4 December

import helper_spotify

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


def sort_songs(songs: list[list[str]], col: int, ascending=True) -> list[list[str]]:
    """Sort a list of spotify songs in place

    Params:
        songs - list of songs
        col - column to sort
        ascending - will sort ascending by default

    Returns: sorted list"""
    # Get songs from an artist
    num_songs = len(songs)
    # Use Selection Sort to sort songs
    for i in range(num_songs):
        candidate_val = helper_spotify.string_to_num(songs[i][col])
        candidate_idx = i
        # check the rest of the list
        for j in range(i + 1, num_songs):
            if ascending:
                this_songs_val = helper_spotify.string_to_num(songs[j][col])
                if this_songs_val < candidate_val:
                    candidate_val = this_songs_val
                    candidate_idx = j
            else:
                this_songs_val = helper_spotify.string_to_num(songs[j][col])
                if this_songs_val > candidate_val:
                    candidate_val = this_songs_val
                    candidate_idx = j

        # swap the current index with the lowest
        songs[i], songs[candidate_idx] = songs[candidate_idx], songs[i]

    return songs


if __name__ == "__main__":
    # Task 1
    # ed_songs = helper_spotify.songs_by_artist("data/spotify2024.csv", "Ed Sheeran")
    # ed_sorted_songs = sort_songs(ed_songs, 11, ascending=False)
    # print("Ed Sheeran's Songs")
    # print("______________________")
    # print("Name \t \t YT Views")
    # for song in ed_sorted_songs:
    #     print(song[0], "\t", song[11])

    # Task 2
    # ed_songs = helper_spotify.songs_by_artist("data/spotify2024.csv", "Ed Sheeran")
    # ed_sorted_songs = sort_songs(ed_songs, 11, ascending=True)
    # print("Ed Sheeran's Songs")
    # print("______________________")
    # print("Name \t \t YT Views")
    # for song in ed_sorted_songs:
    #     print(song[0], "\t", song[11])

    # Task 3
    # ed_songs = helper_spotify.songs_by_artist("data/spotify2024.csv", "Ed Sheeran")
    # ed_sorted_songs = sort_songs(ed_songs, 15, ascending=False)
    # print("Ed Sheeran's Songs")
    # print("______________________")
    # print("Name \t \t Tiktok Views")
    # for song in ed_sorted_songs:
    #     print(song[0], "\t", song[15])

    # Task 4 and 5
    the_songs = helper_spotify.songs_with_the("data/spotify2024.csv", "The " or "the ")
    the_sorted_songs = sort_songs(the_songs, 15, ascending=False)
    print("Songs with The")
    print("______________________")
    print("Name \t \t Tiktok Views")
    for song in the_sorted_songs:
        print(song[0], "\t", song[15])
