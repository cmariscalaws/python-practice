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
    nums1 = [2, 1, 5, 1, 3, 2]
    k1 = 3
    print(f"Test 1: {max_sum_subarray(nums1, k1)} (Expected: 9)")

    # Test 2: All negative numbers
    nums2 = [-2, -1, -5, -1, -3, -2]
    k2 = 2
    print(f"Test 2: {max_sum_subarray(nums2, k2)} (Expected: -2)")

    # Test 3: Window size equals array length
    nums3 = [1, 2, 3, 4]
    k3 = 4
    print(f"Test 3: {max_sum_subarray(nums3, k3)} (Expected: 10)")

    # Test 4: Window size is 1
    nums4 = [5, 3, 8, 1]
    k4 = 1
    print(f"Test 4: {max_sum_subarray(nums4, k4)} (Expected: 8)")

    # Test 5: Invalid k (should raise ValueError)
    try:
        max_sum_subarray([1, 2, 3], 0)
    except ValueError as e:
        print(f"Test 5: Passed (Caught expected error: {e})")
    else:
        print("Test 5: Failed (Did not catch expected error)")

