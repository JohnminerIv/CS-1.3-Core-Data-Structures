#!python
import math
def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):  # o(n) because it iterates through each item until found
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    if array[index] == item:
        return index
    try:
        array[index + 1]
    except:
        return None
    return linear_search_recursive(array, item, index + 1) # o(n) because it iterates through each item until found
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    right = len(array) - 1
    left = 0
    sqrt_len_array = int(math.sqrt(right))
    for i in range(sqrt_len_array + 1):  # o(log n) because it halves the list of items to search in each iteration
        midpoint = left + ((right-left)//2)
        if array[midpoint] == item:
            return midpoint
        elif array[midpoint] < item:
            left = midpoint + 1
        else:
            right = midpoint - 1
    return None
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    if left is None:
        left = 0
        right = len(array) - 1
    midpoint = left + ((right-left)//2)
    if array[midpoint] == item:
        return midpoint
    elif left == right:
        return None
    elif array[midpoint] < item:
        return binary_search_recursive(array, item, midpoint + 1, right)  # o(log n) because it halves the list of items to search in each iteration
    else:
        return binary_search_recursive(array, item, left, midpoint - 1)  # o(log n) because it halves the list of items to search in each iteration

    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
