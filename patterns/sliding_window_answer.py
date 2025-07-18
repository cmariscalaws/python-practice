# O(n) solution for finding
# maximum sum of a subarray of size k
def max_sum(array: [int], k: int) -> int:
    # length of array
    n = len(array)

    # n must be greater than k
    if n <= k:
        print("Invalid")
        return -1

    # compute sum of first window of size k
    window_sum = sum(array[0:k])

    # first sum available
    max_sum = window_sum

    # compute the sums of remaining windows by
    # removing first element of previous
    # window and adding last element of
    # the current window.
    for i in range(n - k):
        window_sum = window_sum - array[i] + array[i + k]
        max_sum = max(max_sum, window_sum)

    return max_sum

if __name__ == '__main__':
    array =  [1, 4, 2, 10, 23, 3, 1, 0, 20]
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