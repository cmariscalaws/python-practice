
from typing import List

def pair_sum_unsorted(nums: List[int], target: int) -> List[int]:
    pass

if __name__ == '__main__':
    nums = [-1, 3, 4, 2]
    target = 3
    expectedPair = [0,2]
    result = []
    result = pair_sum_unsorted(nums, target)
    print(f"nums={nums} target={target} expected={expectedPair} result={result}")
    assert result == expectedPair, f"Expected {expectedPair}, but got {result}"
    
    nums = [-1, 3, 4, 2]
    target = 1
    expectedPair = [0,3]
    result = []
    result = pair_sum_unsorted(nums, target)
    print(f"nums={nums} target={target} expected={expectedPair} result={result}")
    assert result == expectedPair, f"Expected {expectedPair}, but got {result}"
    
    nums = [-1, 3, 4, 2]
    target = 8
    expectedPair = []
    result = []
    result = pair_sum_unsorted(nums, target)
    print(f"nums={nums} target={target} expected={expectedPair} result={result}")
    assert result == expectedPair, f"Expected {expectedPair}, but got {result}"
