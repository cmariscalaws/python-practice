from typing import List

# Merge Sort
# Time: O(nlogn)
# Space: O(n)
# Stable
"""
Merge Sort Algorithm Explanation:
• This function implements the merge sort algorithm which uses divide-and-conquer strategy
• The algorithm works in two main phases:
    1. Divide Phase:
        • Recursively splits the input list into two halves until reaching lists of size 1 or 0
        • Uses midpoint (n//2) to divide the list into left and right sublists

    2. Merge Phase:
        • Uses two pointers (left_pointer and right_pointer) to track positions in left and right sublists
        • Compares elements from both sublists and merges them in sorted order
        • Continues until all elements from both sublists are processed

• Key Characteristics:
    • Time Complexity: O(nlogn) - splits list logn times, each merge takes n operations
    • Space Complexity: O(n) - requires additional space for temporary arrays
    • Stable Sort: Maintains relative order of equal elements
    • Recursive: Uses recursive calls to sort smaller sublists

• Edge Cases Handling:
    • Returns immediately if input list has 0 or 1 elements (base case)
    • Handles cases when one sublist is exhausted by appending remaining elements
"""
def sort_list(unsorted_list: List[int]) -> List[int]:
    n = len(unsorted_list)

    # Base case: A list of size 1 or 0 is already sorted
    if n <= 1:
        return unsorted_list

    # Split the list into left and right halves
    midpoint = n // 2
    left_list = sort_list(unsorted_list[:midpoint])
    right_list = sort_list(unsorted_list[midpoint:])

    result_list = []
    left_pointer, right_pointer = 0, 0

    # Merge the sorted left and right lists with two pointers
    while left_pointer < midpoint or right_pointer < n - midpoint:
        if left_pointer == midpoint:
            # If the left list is empty, append an element from right
            result_list.append(right_list[right_pointer])
            right_pointer += 1
        elif right_pointer == n - midpoint:
            # If the right list is empty, append an element from the left
            result_list.append(left_list[left_pointer])
            left_pointer += 1
        elif left_list[left_pointer] <= right_list[right_pointer]:
            # Append the smaller element from the left list
            result_list.append(left_list[left_pointer])
            left_pointer += 1
        else:
            # Append the smaller element from the right list
            result_list.append(right_list[right_pointer])
            right_pointer += 1

    return result_list


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

