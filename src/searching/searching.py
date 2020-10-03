# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, *args):
    # Your code here
    return search_recursive(0, len(arr), arr, target)


def search_recursive(left, right, arr, target):
    if left > right or len(arr) == 0:
        return -1
    middle = (left + right) // 2
    value = arr[middle]
    if left == right:
        if target == value:
            return middle
        else: return -1
    if value == target:
        return middle
    elif target < value:
        return search_recursive(left, middle, arr, target)
    else:
        return search_recursive(middle + 1, right, arr, target)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    if arr[-1] > arr[0]:
        return binary_search(arr, target)

    else: return agnostic_search_recursive(0, len(arr), arr, target)


def agnostic_search_recursive(left, right, arr, target):
    if left > right or len(arr) == 0:
        return -1
    middle = (left + right) // 2
    value = arr[middle]
    if left == right:
        if target == value:
            return middle
        else: return -1
    if value == target:
        return middle
    elif target < value:
        return agnostic_search_recursive(middle + 1, right, arr, target)
    else:
        return agnostic_search_recursive(left, middle, arr, target)

