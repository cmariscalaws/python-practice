
from typing import List

def pair_sum_unsorted(nums: List[int], target: int) -> List[int]:
    num_dic = {}

    for i, num in enumerate(nums):
        complement = target - num
        if (complement in num_dic):
            return [num_dic[complement], i]
        else:
            num_dic[num] = i

    return []

if __name__ == '__main__':
    nums = [-1, 3, 4, 2]
    target = 3
    expectedPair = [0,2]
    result = []

    result = pair_sum_unsorted(nums, target)

    print(result)
    assert result == expectedPair, f"Expected {expectedPair}, but got {result}"
