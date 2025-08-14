
from typing import List

def find_occurences(nums: List[int], target: int) -> int:
    pass

if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    expected = [3, 4]
    result = find_occurences(nums, target)
    print(f"nums:{nums} target:{target} expected:{expected} result: {result}")
    assert result == expected, f"Expected {expected}, but got {result}"

    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    expected = [-1, -1]
    result = find_occurences(nums, target)
    print(f"nums:{nums} target:{target} expected:{expected} result: {result}")
    assert result == expected, f"Expected {expected}, but got {result}"

    nums = []
    target = 0
    expected = [-1, -1]
    result = find_occurences(nums, target)
    print(f"nums:{nums} target:{target} expected:{expected} result: {result}")
    assert result == expected, f"Expected {expected}, but got {result}"




