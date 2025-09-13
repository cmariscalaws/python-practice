from typing import List

# Two Pointers Technique for Pair Sum in Sorted Array
# Time: O(n)
# Space: O(1)
# This function finds two indices in a sorted array such that the sum of the elements at those indices equals the target.
# It uses a two-pointer approach, starting from both ends of the array and moving towards the
# center based on the sum comparison with the target.
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


