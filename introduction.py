"""
Using Grokking algorithm book as a study material
Lesson One binary search algorithm
"""


def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high)
        guess = list[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = ["antman", "batman", "cat woman",
           "captain america", "ironman", "zerks"]


print(binary_search(my_list, 3))
