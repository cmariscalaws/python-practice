
from typing import List

"""
Finds the index of the first element in a sorted list that is not smaller than the target.

Uses binary search to efficiently locate the smallest index where nums[index] >= target.
If no such element exists, returns -1.

Args:
    nums (List[int]): A sorted list of integers.
    target (int): The target value to compare.

Returns:
    int: The index of the first element not smaller than target, or -1 if not found.
"""
def first_not_smaller(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    not_smaller = -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] >= target:
            not_smaller = mid
            right = mid - 1
        else:
            left = mid + 1

    return not_smaller

if __name__ == '__main__':
    nums = [1, 3, 3, 5, 8, 8, 10]
    target = 2
    expected = 1
    result = first_not_smaller(nums, target)
    print(f"nums:{nums} target:{target} expected:{expected} result: {result}")
    assert result == expected, f"Expected {expected}, but got {result}"

    nums = [2, 3, 5, 7, 11, 13, 17, 19]
    target = 6
    expected = 3
    result = first_not_smaller(nums, target)
    print(f"nums:{nums} target:{target} expected:{expected} result: {result}")
    assert result == expected, f"Expected {expected}, but got {result}"


