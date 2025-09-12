"""
Sliding Window Example: Maximum Sum Subarray of Size K

Problem Statement:
Given an array of integers nums and an integer k, find the maximum sum of any contiguous subarray of size k.

Sliding Window Algorithm:
- The sliding window technique is used to efficiently solve problems involving contiguous subarrays or substrings.
- Instead of recalculating the sum for every window, we slide the window by one element at a time, subtracting the element that is left behind and adding the new element.

Time Complexity: O(n), where n is the length of the array.

Example:
nums = [2, 1, 5, 1, 3, 2], k = 3
Output: 9 (subarray [5, 1, 3])
"""

def max_sum_subarray(nums, k):
    pass

# --- Test Cases ---
if __name__ == "__main__":
    # Test 1: Example from docstring
    nums = [2, 1, 5, 1, 3, 2]
    k = 3
    expected = 9
    result = max_sum_subarray(nums, k)
    print(f"Test 1: {result} (Expected: {expected})")
    assert result == expected, f"Test 1 Failed: Expected {expected}, got {result}"

    # Test 2: All negative numbers
    nums = [-2, -1, -5, -1, -3, -2]
    k = 2
    expected = -3  # Corrected expected value
    result = max_sum_subarray(nums, k)
    print(f"Test 2: {result} (Expected: {expected})")
    assert result == expected, f"Test 2 Failed: Expected {expected}, got {result}"

    # Test 3: Window size equals array length
    nums = [1, 2, 3, 4]
    k = 4
    expected = 10
    result = max_sum_subarray(nums, k)
    print(f"Test 3: {result} (Expected: {expected})")
    assert result == expected, f"Test 3 Failed: Expected {expected}, got {result}"

    # Test 4: Window size is 1
    nums = [5, 3, 8, 1]
    k = 1
    expected = 8
    result = max_sum_subarray(nums, k)
    print(f"Test 4: {result} (Expected: {expected})")
    assert result == expected, f"Test 4 Failed: Expected {expected}, got {result}"

    # Test 5: Invalid k (should raise ValueError)
    try:
        max_sum_subarray([1, 2, 3], 0)
    except ValueError as e:
        print(f"Test 5: Passed (Caught expected error: {e})")
    else:
        assert False, "Test 5: Failed (Did not catch expected error)"

