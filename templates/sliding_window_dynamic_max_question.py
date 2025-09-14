def max_subarray_sum_leq_target(nums, target):
    pass


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
