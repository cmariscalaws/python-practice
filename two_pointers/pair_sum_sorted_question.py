
from typing import List

def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    pass

if __name__ == '__main__':
    nums = [-5,-2, 3, 4, 6]
    expected = [2, 3]
    result = pair_sum_sorted(nums, 7)

    print(result)
    assert result == expected, f"Expected {expected}, but got {result}"
