
from typing import List

def unique_occurrences(nums: List[int]) -> bool:
    pass

if __name__ == '__main__':
    nums = [1,2,2,1,1,3]
    expected = True
    result = unique_occurrences(nums)
    print(f"nums={nums} expected={expected} result={result}")
    assert result == expected, f"Expected {expected}, but got {result}"

    nums = [1, 2]
    expected = False
    result = unique_occurrences(nums)
    print(f"nums={nums} expected={expected} result={result}")
    assert result == expected, f"Expected {expected}, but got {result}"

    nums = [-3,0,1,-3,1,1,1,-3,10,0]
    expected = True
    result = unique_occurrences(nums)
    print(f"nums={nums} expected={expected} result={result}")
    assert result == expected, f"Expected {expected}, but got {result}"


