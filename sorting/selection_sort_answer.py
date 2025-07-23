from typing import List

# Selection Sort
# Time: O(n^2)
# Space: O(1)

'''
Selection Sort Algorithm Explanation:
* The algorithm divides the input list into two parts:
  - The sorted portion (left side)
  - The unsorted portion (right side)

* For each iteration:
  1. Start with the current position (i) as the assumed minimum
  2. Scan the rest of the list (from i to end) to find the actual minimum
  3. Swap the found minimum with the current position (i)
  4. The sorted portion grows by one element

* Key Characteristics:
  - In-place algorithm (modifies original list)
  - Stable sort (maintains relative order of equal elements)
  - Time Complexity: O(n²) for all cases
  - Space Complexity: O(1) as it only uses a few variables

* Example Process for [5,3,1,2,4]:
  1. First pass: find min(5,3,1,2,4)=1 → [1,3,5,2,4]
  2. Second pass: find min(3,5,2,4)=2 → [1,2,5,3,4]
  3. Third pass: find min(5,3,4)=3 → [1,2,3,5,4]
  4. Fourth pass: find min(5,4)=4 → [1,2,3,4,5]
  5. Fifth pass: only 5 remains → done
'''
def sort_list(unsorted_list: List[int]) -> List[int]:
    n = len(unsorted_list)
    for i in range(n):
        # Assume the current position as minimum
        min_index = i

        # Find the minimum element's index from the rest of the list
        for j in range(i, n):
            if unsorted_list[j] < unsorted_list[min_index]:
                min_index = j

        # Swap the minimum element with the first element
        unsorted_list[i], unsorted_list[min_index] = unsorted_list[min_index], unsorted_list[i]

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

