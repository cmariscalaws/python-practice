
from typing import List

def find_first_occurence(nums: List[int], target: int) -> int:
    pass

if __name__ == '__main__':
    nums = [1, 3, 3, 3, 3, 6, 10, 10, 100]
    target = 3
    expected = 1
    result = find_first_occurence(nums, target)
    print(f"nums:{nums} target:{target} expected:{expected} result: {result}")
    assert result == expected, f"Expected {expected}, but got {result}"

    nums = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    target = 1
    expected = 0
    result = find_first_occurence(nums, target)
    print(f"nums:{nums} target:{target} expected:{expected} result: {result}")
    assert result == expected, f"Expected {expected}, but got {result}"

    nums = [1, 22, 22, 33, 50, 100, 20000]
    target = 33
    expected = 3
    result = find_first_occurence(nums, target)
    print(f"nums:{nums} target:{target} expected:{expected} result: {result}")
    assert result == expected, f"Expected {expected}, but got {result}"

    nums = [4, 6, 7, 7, 7, 20]
    target = 8
    expected = -1
    result = find_first_occurence(nums, target)
    print(f"nums:{nums} target:{target} expected:{expected} result: {result}")
    assert result == expected, f"Expected {expected}, but got {result}"

    nums = [6, 7, 9, 10, 10, 10, 90]
    target = 10
    expected = 3
    result = find_first_occurence(nums, target)
    print(f"nums:{nums} target:{target} expected:{expected} result: {result}")
    assert result == expected, f"Expected {expected}, but got {result}"


