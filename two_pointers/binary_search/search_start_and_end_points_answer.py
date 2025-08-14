
from typing import List

def find_occurrences(nums: List[int], target: int) -> List[int]:
    # Initialize pointers for binary search and result variables
    left, right = 0, len(nums) - 1
    first_occurrence, last_occurrence = -1, -1

    # Binary search to find the first occurrence of target
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            # Update first_occurrence and continue searching left half
            first_occurrence = mid
            right = mid - 1
        elif nums[mid] > target:
            # Target is in the left half
            right = mid - 1
        else:
            # Target is in the right half
            left = mid + 1

    # Reset pointers for binary search to find last occurrence
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            # Update last_occurrence and continue searching right half
            last_occurrence = mid
            left = mid + 1
        elif nums[mid] > target:
            # Target is in the left half
            right = mid - 1
        else:
            # Target is in the right half
            left = mid + 1

    # Return the indices of first and last occurrence
    return [first_occurrence, last_occurrence]

if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    expected = [3, 4]
    result = find_occurrences(nums, target)
    print(f"nums:{nums} target:{target} expected:{expected} result: {result}")
    assert result == expected, f"Expected {expected}, but got {result}"

    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    expected = [-1, -1]
    result = find_occurrences(nums, target)
    print(f"nums:{nums} target:{target} expected:{expected} result: {result}")
    assert result == expected, f"Expected {expected}, but got {result}"

    nums = []
    target = 0
    expected = [-1, -1]
    result = find_occurrences(nums, target)
    print(f"nums:{nums} target:{target} expected:{expected} result: {result}")
    assert result == expected, f"Expected {expected}, but got {result}"




