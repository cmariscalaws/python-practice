
from typing import List

def binary_search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

if __name__ == '__main__':
    nums = [1, 3, 5, 7, 8]
    expected = 2
    result = binary_search(nums, 5)
    print(result)
    assert result == expected, f"Expected {expected}, but got {result}"

    nums = [1, 2, 3, 4, 5, 6, 7]
    expected = -1
    result = binary_search(nums, 0)
    print(result)
    assert result == expected, f"Expected {expected}, but got {result}"

    nums = [2, 8, 89, 120, 1000]
    expected = 3
    result = binary_search(nums, 120)
    print(result)
    assert result == expected, f"Expected {expected}, but got {result}"

    nums = [10, 20]
    expected = 1
    result = binary_search(nums, 20)
    print(result)
    assert result == expected, f"Expected {expected}, but got {result}"

    nums = [1]
    expected = 0
    result = binary_search(nums, 1)
    print(result)
    assert result == expected, f"Expected {expected}, but got {result}"

    nums = []
    expected = -1
    result = binary_search(nums, 1)
    print(result)
    assert result == expected, f"Expected {expected}, but got {result}"

    nums = [1, 2, 3, 4, 5]
    expected = -1
    result = binary_search(nums, 10)
    print(result)
    assert result == expected, f"Expected {expected}, but got {result}"
