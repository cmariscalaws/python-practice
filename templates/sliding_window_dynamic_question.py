"""
Sliding Window Example: Smallest Subarray with Sum at Least S (Dynamic Window)

Problem Statement:
Given an array of positive integers nums and a positive integer s, find the minimal length of a contiguous subarray of which the sum is at least s. If there is no such subarray, return 0 instead.

Sliding Window Algorithm (Dynamic Window):
- The window expands to include new elements until the sum is at least s.
- Then, it contracts from the left to find the smallest window that still satisfies the sum condition.
- This approach is efficient for problems where the window size is not fixed and depends on a condition.

Time Complexity: O(n), where n is the length of the array.

Example:
nums = [2, 3, 1, 2, 4, 3], s = 7
Output: 2 (subarray [4, 3])
"""

def min_subarray_len(s, nums):
    pass

# --- Test Cases ---
if __name__ == "__main__":
    # Test 1: Example from docstring
    nums = [2, 3, 1, 2, 4, 3]
    s = 7
    expected = 2  # [4, 3]
    result = min_subarray_len(s, nums)
    print(f"Test 1: {result} (Expected: {expected})")
    assert result == expected, f"Test 1 Failed: Expected {expected}, got {result}"

    # Test 2: No subarray meets the sum
    nums = [1, 1, 1, 1]
    s = 10
    expected = 0
    result = min_subarray_len(s, nums)
    print(f"Test 2: {result} (Expected: {expected})")
    assert result == expected, f"Test 2 Failed: Expected {expected}, got {result}"

    # Test 3: Whole array is needed
    nums = [1, 2, 3, 4]
    s = 10
    expected = 4
    result = min_subarray_len(s, nums)
    print(f"Test 3: {result} (Expected: {expected})")
    assert result == expected, f"Test 3 Failed: Expected {expected}, got {result}"

    # Test 4: Single element meets the sum
    nums = [1, 10, 5, 2]
    s = 10
    expected = 1
    result = min_subarray_len(s, nums)
    print(f"Test 4: {result} (Expected: {expected})")
    assert result == expected, f"Test 4 Failed: Expected {expected}, got {result}"

    # Test 5: Invalid s (should raise ValueError)
    try:
        min_subarray_len(0, [1, 2, 3])
    except ValueError as e:
        print(f"Test 5: Passed (Caught expected error: {e})")
    else:
        assert False, "Test 5: Failed (Did not catch expected error)"
