from typing import List

# quick sort
# time: O(nlogn)
# space: O(logn)
# stable
# utilizes two pointer technique
"""
QuickSort Implementation:
• Algorithm Overview:
    - Uses divide-and-conquer strategy to sort the list
    - Picks a 'pivot' element and partitions other elements into two sub-arrays
    - Elements less than pivot go to left sub-array
    - Elements greater than pivot go to right sub-array

• Implementation Details:
    - Uses the last element as the pivot
    - Employs two pointers technique for partitioning
    - Recursively sorts the sub-arrays

• Time Complexity:
    - Average case: O(n log n)
    - Worst case: O(n²) when list is already sorted

• Space Complexity:
    - O(log n) due to recursive call stack

• Algorithm Steps:
    1. If array size is 1 or less, it's already sorted
    2. Choose last element as pivot
    3. Partition:
       - Move smaller elements to left of pivot
       - Move larger elements to right of pivot
    4. Place pivot in its final position
    5. Recursively sort left and right portions

• Features:
    - In-place sorting (modifies original list)
    - Not stable (equal elements may change relative order)
    - Efficient for random data

Args:
    unsorted_list: List of integers to be sorted

Returns:
    Sorted list in ascending order
"""
def sort_list_interval(unsorted_list: List[int], start: int, end: int) -> None:
    # If a segment is 1 or 0, it's sorted
    if end - start <= 1:
        return

    # Using the last element as the pivot
    pivot = unsorted_list[end - 1]
    start_ptr, end_ptr = start, end - 1

    # Partitioning process
    while start_ptr < end_ptr:
        # Find the next element from the left that is larger than the pivot
        while unsorted_list[start_ptr] < pivot and start_ptr < end_ptr:
            start_ptr += 1

        # Find the next element from the right that is smaller than or equal to the pivot
        while unsorted_list[end_ptr] >= pivot and start_ptr < end_ptr:
            end_ptr -= 1

        # Swap if pointers haven't met
        unsorted_list[start_ptr], unsorted_list[end_ptr] = unsorted_list[end_ptr], unsorted_list[start_ptr]

    # Place pivot in its final position
    unsorted_list[start_ptr], unsorted_list[end - 1] = unsorted_list[end - 1], unsorted_list[start_ptr]

    # Recursively sort left and right of the pivot
    sort_list_interval(unsorted_list, start, start_ptr)
    sort_list_interval(unsorted_list, start_ptr + 1, end)

def sort_list(unsorted_list: List[int]) -> List[int]:
    sort_list_interval(unsorted_list, 0, len(unsorted_list))
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

