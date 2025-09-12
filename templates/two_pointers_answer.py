from typing import List

# Two Pointers Technique for Pair Sum in Sorted Array
# Time: O(n)
# Space: O(1)
# This function finds two indices in a sorted array such that the sum of the elements at those indices equals the target.
# It uses a two-pointer approach, starting from both ends of the array and moving towards the
# center based on the sum comparison with the target.
def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) - 1

    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return [left, right]
        elif sum < target:
            left += 1
        else:
            right -= 1

    return []

if __name__ == '__main__':
    nums = [-5,-2, 3, 4, 6]
    expected = [2, 3]
    result = pair_sum_sorted(nums, 7)

    print(result)
    assert result == expected, f"Expected {expected}, but got {result}"


