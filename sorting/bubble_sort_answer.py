from typing import List

# Bubble Sort
# Time: O(n^2)
# Space: O(1)
# Stable

'''
Bubble Sort Algorithm Explanation:
* Good for sorting lists that are almost sorted
* The algorithm iterates through the list multiple times, comparing adjacent elements
* In each iteration:
    - Compares pairs of adjacent elements from start to end
    - If the left element is greater than the right element, they are swapped
    - This "bubbles up" the largest element to the end of the unsorted portion
* Optimization features:
    - Uses a 'swapped' flag to detect if list is already sorted
    - Early termination if no swaps occur in a pass
    - Reduces the comparison range in each pass as larger elements are placed correctly
* Implementation details:
    - Outer loop: Runs n-1 times in reverse order (controls sorted portion)
    - Inner loop: Compares adjacent elements in the unsorted portion
    - Uses simultaneous assignment for clean swap operations
* Performance characteristics:
    - Time Complexity: O(n²) - where n is the length of the list
    - Space Complexity: O(1) - sorts in-place
    - Stable sort: Maintains relative order of equal elements
'''
def sort_list(unsorted_list: List[int]) -> List[int]:
    n = len(unsorted_list)

    # Iterate through all list elements in reversed order
    for i in reversed(range(n)):
        # Track whether a swap occurred in this pass
        swapped = False
        for j in range(i):
            # Swap if the element found is greater than the next element
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
                swapped = True

        # If no two elements were swapped, the list is sorted
        if not swapped:
            return unsorted_list

    return unsorted_list


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

