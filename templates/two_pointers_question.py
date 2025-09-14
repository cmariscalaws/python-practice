from typing import List

def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    pass

if __name__ == '__main__':
    nums = [-5,-2, 3, 4, 6]
    expected = [2, 3]
    target = 7
    result = pair_sum_sorted(nums, target)
    print(f"nums: {nums}, target: {target}, expected: {expected}, result: {result}")
    assert result == expected, f"Expected {expected}, but got {result}"

    nums = [-5,-2, 3, 4, 6]
    expected = []
    target = 12
    result = pair_sum_sorted(nums, target)
    print(f"nums: {nums}, target: {target}, expected: {expected}, result: {result}")
    assert result == expected, f"Expected {expected}, but got {result}"

    nums = []
    expected = []
    target = 7
    result = pair_sum_sorted(nums, 7)
    print(f"nums: {nums}, target: {target}, expected: {expected}, result: {result}")
    assert result == expected, f"Expected {expected}, but got {result}"

    nums = [-5,-2, 3, 4, 6]
    expected = [3, 4]
    target = 10
    result = pair_sum_sorted(nums, target)
    print(f"nums: {nums}, target: {target}, expected: {expected}, result: {result}")
    assert result == expected, f"Expected {expected}, but got {result}"

    nums = [-5,-2, 3, 4, 6]
    expected = [0, 4]
    target = 1
    result = pair_sum_sorted(nums, target)
    print(f"nums: {nums}, target: {target}, expected: {expected}, result: {result}")
    assert result == expected, f"Expected {expected}, but got {result}"


