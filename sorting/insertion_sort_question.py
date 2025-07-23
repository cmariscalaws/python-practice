from typing import List

def sort_list(unsorted_list: List[int]) -> int:
    pass

if __name__ == '__main__':
    unsorted_list = [5, 3, 1, 2, 4]
    expectedResult = [1, 2, 3, 4, 5]
    result = sort_list(unsorted_list)
    print(result)
    assert result == expectedResult, f"Expected {expectedResult}, but got {result}"

    unsorted_list = [8, 10, 1, 3, 4, 6, 9, 2, 7, 5]
    expectedResult = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = sort_list(unsorted_list)
    print(result)
    assert result == expectedResult, f"Expected {expectedResult}, but got {result}"

    unsorted_list = [8466, 1024, 7744, 4668, 2011, 7744, 6861, 8964, 1100]
    expectedResult = [1024, 1100, 2011, 4668, 6861, 7744, 7744, 8466, 8964]
    result = sort_list(unsorted_list)
    print(result)
    assert result == expectedResult, f"Expected {expectedResult}, but got {result}"

