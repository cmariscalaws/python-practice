
from typing import List

def remove_duplicates(nums: List[int]) -> List[int]:
    slow = 0

    for fast in range(len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return nums[0: slow + 1]

if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2]
    expected = [0, 1, 2]
    result = remove_duplicates(nums)
    print(f"nums={nums}, expected={expected}, result={result}")
    assert result == expected, f"Expected {expected}, but got {result}"

    nums = [1, 2, 3]
    expected = [1, 2, 3]
    result = remove_duplicates(nums)
    print(f"nums={nums}, expected={expected}, result={result}")
    assert result == expected, f"Expected {expected}, but got {result}"

    nums = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    expected = [1]
    result = remove_duplicates(nums)
    print(f"nums={nums}, expected={expected}, result={result}")
    assert result == expected, f"Expected {expected}, but got {result}"

    nums = [0, 0, 1, 1, 2, 2, 200, 200, 300, 300]
    expected = [0, 1, 2, 200, 300]
    result = remove_duplicates(nums)
    print(f"nums={nums}, expected={expected}, result={result}")
    assert result == expected, f"Expected {expected}, but got {result}"
