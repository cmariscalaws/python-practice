from typing import List

def shift_zeros_to_the_end(nums: List[int]) -> None:

    print(f"before: {nums}")
    pass

    print(f"after: {nums}")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1, 0, 2, 0, 0, 7]
    shift_zeros_to_the_end(nums)
    assert nums == [1, 2, 7, 0, 0, 0]

    nums = [3, 1, 0, 1, 3, 8, 9]
    shift_zeros_to_the_end(nums)
    assert nums == [3, 1, 1, 3, 8, 9, 0]

    nums = [0, 0, 9, 4, 0, 0, 3, 8, 0]
    shift_zeros_to_the_end(nums)
    assert nums == [9, 4, 3, 8, 0, 0, 0, 0, 0]
