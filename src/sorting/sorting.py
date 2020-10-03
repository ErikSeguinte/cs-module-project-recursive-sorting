from typing import List
from collections import deque
# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    arrA = deque(arrA)
    arrB = deque(arrB)
    merged = []

    # Your code here
    while arrA or arrB:
        if not arrB:
            merged.append(arrA.popleft())
            continue

        if not arrA:
            merged.append(arrB.popleft())
            continue

        if arrA[0] < arrB[0]:
            merged.append(arrA.popleft())
        else:
            merged.append(arrB.popleft())


    return merged

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2

    left = arr[:middle]
    left_merged = merge_sort(left)

    right = arr[middle:]
    right_merged = merge_sort(right)
    merged = merge(left_merged, right_merged)

    return merged

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here
#     l = start
#     l_end = mid
#
#     r = mid
#     r_end = end
#
#     i = start
#
#     while (l < l_end) or (r < l_end):
#         if arr[r_start] > arr[l_start]:
#             arr[l], arr[r] = arr[r_start], arr



# def merge_sort_in_place(arr, l, r):
#     # Your code here

