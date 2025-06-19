
from typing import List

def triplet_sum(nums: List[int]) -> List[List[int]]:
    pass

if __name__ == '__main__':
    nums = [0,-1,2,-3,1]
    expected = [[-3,1,2],[-1,0,1]]
    result = []

    result = triplet_sum(nums)

    print(result)
    assert result == expected, f"Expected {expected}, but got {result}"
