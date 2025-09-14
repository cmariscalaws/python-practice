"""
Sliding Window Dynamic Max Problem

Given an array of integers and a target sum, find the maximum sum of any contiguous subarray
whose sum is less than or equal to the target. The window size can increase or decrease dynamically
based on the sum constraint.

This is a classic use-case for the sliding window technique, where the window expands to include
new elements and contracts from the left when the sum exceeds the target.

Algorithm:
1. Initialize two pointers (left, right) to represent the window.
2. Expand the window by moving 'right' and adding nums[right] to the current sum.
3. If the sum exceeds the target, shrink the window from the left by moving 'left' and subtracting nums[left].
4. Track the maximum sum found that does not exceed the target.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def max_subarray_sum_leq_target(nums, target):
    """
    Returns the maximum sum of any contiguous subarray with sum <= target.

    Args:
        nums (List[int]): List of integers.
        target (int): The target sum.

    Returns:
        int: The maximum subarray sum not exceeding target.
    """
    max_sum = 0
    current_sum = 0
    left = 0

    for right in range(len(nums)):
        current_sum += nums[right]
        # Shrink window from the left if sum exceeds target
        while current_sum > target and left <= right:
            current_sum -= nums[left]
            left += 1
        # Update max_sum if current_sum is valid
        if current_sum <= target:
            max_sum = max(max_sum, current_sum)
    return max_sum

# In-file tests
if __name__ == "__main__":
    # Test 1: Basic case
    nums = [2, 1, 3, 4, 1, 1, 5]
    target = 7
    print(f"Test 1: nums={nums}, target={target}")  # Expected output: 7
    expected = 7
    result = max_subarray_sum_leq_target(nums, target)
    print(f"Result: {result}, Expected: {expected}")
    assert result == expected  # [3,4], [4,1,1,1], etc.

    # Test 2: All elements less than target
    nums = [1, 2, 3]
    target = 10
    print(f"Test 2: nums={nums}, target={target}")
    expected = 6
    result = max_subarray_sum_leq_target(nums, target)
    print(f"Result: {result}, Expected: {expected}")
    assert result == expected  # [1,2,3]

    # Test 3: No subarray less than or equal to target
    nums = [8, 9, 10]
    target = 7
    print(f"Test 3: nums={nums}, target={target}")
    expected = 0
    result = max_subarray_sum_leq_target(nums, target)
    print(f"Result: {result}, Expected: {expected}")
    assert result == expected

    # Test 4: Single element equals target
    nums = [5, 1, 2, 7]
    target = 7
    print(f"Test 4: nums={nums}, target={target}")
    expected = 7
    result = max_subarray_sum_leq_target(nums, target)
    print(f"Result: {result}, Expected: {expected}")
    assert result == expected  # [7]

    # Test 5: Empty array
    nums = []
    target = 5
    print(f"Test 5: nums={nums}, target={target}")
    expected = 0
    result = max_subarray_sum_leq_target(nums, target)
    print(f"Result: {result}, Expected: {expected}")
    assert result == expected

    print("All tests passed.")
