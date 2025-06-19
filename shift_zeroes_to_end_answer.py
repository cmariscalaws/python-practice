from typing import List

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def shift_zeros_to_the_end(nums: List[int]) -> None:
    # Keep track of position where we should place next non-zero element
    non_zero_pos = 0

    # Move all non-zero elements to the front
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_pos], nums[i] = nums[i], nums[non_zero_pos]
            non_zero_pos += 1

    print(nums)


def shift_zeros_to_the_end2(nums: List[int]) -> None:
    # left pointer: where to place next non-zero number
    # right pointer: scanning through the array
    left = 0

    # First pass: move all non-zero numbers to the front
    for right in range(len(nums)):
        if nums[right] != 0:
            # Only swap if pointers are different
            if left != right:
                nums[left], nums[right] = nums[right], nums[left]
            left += 1

    print(nums)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [0, 1, 0, 2, 3]
    shift_zeros_to_the_end2(nums)

    assert nums == [1, 2, 3, 0, 0]

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
