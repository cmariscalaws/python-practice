# essentially sorted 2 sum problem 2 pointers
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    # <= because left and right could point to the same element, < would miss it
    while left <= right:

        # double slash for integer division in python 3,
        # we don't have to worry about integer `left + right` overflow
        # since python integers can be arbitrarily large
        mid = (left + right) // 2

        # found target, return its index
        if arr[mid] == target:
            return mid
        # middle less than target, discard left half by making left search boundary `mid + 1`
        elif arr[mid] < target:
            left = mid + 1
        # middle greater than target, discard right half by making right search boundary `mid - 1`
        else:
            right = mid - 1
    return -1