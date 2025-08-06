
from typing import List

def first_not_smaller(nums: List[int], target: int) -> int:
    pass

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

    nums = [0]
    target = 0
    expected = 0
    result = first_not_smaller(nums, target)
    print(f"nums:{nums} target:{target} expected:{expected} result: {result}")
    assert result == expected, f"Expected {expected}, but got {result}"

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 10
    expected = 9
    result = first_not_smaller(nums, target)
    print(f"nums:{nums} target:{target} expected:{expected} result: {result}")
    assert result == expected, f"Expected {expected}, but got {result}"

    nums = [1, 2, 2, 2, 2, 2, 2, 3, 5, 8, 8, 10]
    target = 2
    expected = 1
    result = first_not_smaller(nums, target)
    print(f"nums:{nums} target:{target} expected:{expected} result: {result}")
    assert result == expected, f"Expected {expected}, but got {result}"


