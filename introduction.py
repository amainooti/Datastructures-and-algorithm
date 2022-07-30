"""
Using Grokking algorithm book as a study material
Lesson One binary search algorithm vs linear search.
Binary search has a big O of O(logn) while linear search has a
big O of O(n)
"""


# binary search implementation

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


my_list = [1, 2, 3, 4, 5, 6, 7]


print(binary_search(my_list, 3))


# simple search implementation

def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return f"{target} was found at position: {i}"

    return "Not found in list"


list = [12, 7, 19, 25, 22, 8, 17, 121, 190, 222, 90, 0]

my_item = linear_search(list, 8)
print(my_item)
