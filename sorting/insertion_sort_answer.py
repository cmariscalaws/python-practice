from typing import List

# Insertion Sort
# Time: O(n^2)
# Space: O(1)
# Not Stable

'''
### Key Characteristics
- **Time Complexity**: O(n²)
- **Space Complexity**: O(1)
- **In-place sorting**: Modifies the original list
- **Input Type**: List of integers
- **Return Type**: Sorted list of integers
- **good for sorting lists that are almost sorted
### How It Works
1. **Outer Loop**:
- Iterates through each element in the list from index 0 to n-1
- represents the current position we're trying to insert the element at `i`
2. **Inner While Loop**:
- Compares the current element with previous elements
- Continues as long as:
    - We haven't reached the start of the list () `current > 0`
    - The current element is smaller than the previous element

3. **Swap Operation**:
- Swaps the current element with the previous element if it's smaller
- Continues moving the element backward until it's in the correct position
'''
def sort_list(unsorted_list: List[int]) -> List[int]:
    for i in range(len(unsorted_list)):
        current = i
        # gets the smallest element and inserts it at current index
        while current > 0 and unsorted_list[current] < unsorted_list[current - 1]:
            #swaps current smaller element with the element before it
            unsorted_list[current], unsorted_list[current - 1] = unsorted_list[current - 1], unsorted_list[current]
            current -= 1

    return unsorted_list

if __name__ == '__main__':
    unsorted_list =  [5, 3, 1, 2, 4]
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