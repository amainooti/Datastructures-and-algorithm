'''
    SELECTION SORT ALGORITHM
    This algorithm checks every element for either the largest or the smallest number
    and does this n number of times until it sorts the list. It has a big O of O(n x n)
'''

# find the smallest number


# def find_smallest(arr):
#     smallest = arr[0]
#     smallest_index = 0
#     for item in range(1, len(arr)):
#         if arr[item] < smallest:
#             smallest = arr[item]
#             smallest_index = item
#     return smallest_index


# section sort


# def selection_sort(arr):
#     newArr = []
#     for i in range(len(arr)):
#         smallest = find_smallest(arr)
#         newArr.append(arr.pop(smallest))
#     return newArr


def smallest(arr):
    smallest_element = arr[0]
    smallest_index = 0
    for item in range(len(arr)):
        if arr[item] < smallest_element:
            smallest_element = arr[item]
            smallest_index = item
    return smallest_index


def selection_sort(arr):
    new_arr = []
    for item in range(len(arr)):
        smallest_item = smallest(arr)
        # remove the arr from from the original arr
        removed_list = arr.pop(smallest_item)
        new_arr.append(removed_list)
    return new_arr


arr = [12, 10, 13, 8, 9, 14]

print(selection_sort(arr))
