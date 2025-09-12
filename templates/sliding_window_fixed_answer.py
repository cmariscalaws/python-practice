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
    """
    Returns the maximum sum of any contiguous subarray of size k.
    Args:
        nums (List[int]): The input array.
        k (int): The size of the window.
    Returns:
        int: The maximum sum found.
    """
    n = len(nums)

    print(f"Entering max_sum_subarray: nums={nums}, n={n}, k={k}", flush=True)

    if n < k or k <= 0:
        raise ValueError("Window size k must be positive and less than or equal to the length of the array.")

    current_sum = 0
    max_sum = float('-inf')  # Initialize with negative infinity

    # 1. Expand the window (Initial Window)
    for i in range(k):
        current_sum += nums[i]
    max_sum = current_sum
    print(f"initial window (sum of elements, k={k}): current_sum={current_sum}", flush=True)

    # 2. Slide the Window
    left = 0
    right = k
    while right < n:
        # Shrink the window
        current_sum -= nums[left]
        print(f"decrease window (left:{left}): current_sum={current_sum}", flush=True)
        left += 1

        # Expand the window
        current_sum += nums[right]
        print(f"increase window (right:{right}): current_sum={current_sum}", flush=True)
        right += 1

        # Process the current window
        max_sum = max(max_sum, current_sum)
        print(f"max_sum={max_sum}", flush=True)

    return max_sum

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
