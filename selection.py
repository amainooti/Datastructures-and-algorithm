'''
    SELECTION SORT ALGORITHM
    This algorithm checks every element for either the largest or the smallest number
    and does this n number of times until it sorts the list. It has a big O of O(n x n)
'''

# find the smallest number


def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for item in range(1, len(arr)):
        if arr[item] < smallest:
            smallest = arr[item]
            smallest_index = item
    return smallest_index


# section sort


def selection_sort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


arr = [12, 10, 13, 8, 9, 14]

print(selection_sort(arr))
