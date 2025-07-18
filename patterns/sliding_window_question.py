from typing import List

# O(n) solution for finding
# maximum sum of a subarray of size k
def max_sum(array: [int], k: int) -> int:
    n = len(array)

    if n < k:
        return -1

    window_sum = sum(array[0:k])

    if n == k:
        return window_sum

    max_sum = window_sum

    for i in range(n - k):
        window_sum = window_sum - array[i] + array[k + i]
        max_sum = max(max_sum, window_sum)

    return max_sum


if __name__ == '__main__':
    array = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    expectedResult = 39
    result = max_sum(array, k)
    print(result)
    assert result == expectedResult, f"Expected {expectedResult}, but got {result}"

    array = [100, 200, 300, 400]
    k = 2
    expectedResult = 700
    result = max_sum(array, k)
    print(result)
    assert result == expectedResult, f"Expected {expectedResult}, but got {result}"

    array = [2, 3]
    k = 3
    expectedResult = -1
    result = max_sum(array, k)
    print(result)
    assert result == expectedResult, f"Expected {expectedResult}, but got {result}"

    array = [100, 200, 300, 400]
    k = 4
    expectedResult = 1000
    result = max_sum(array, k)
    print(result)
    assert result == expectedResult, f"Expected {expectedResult}, but got {result}"