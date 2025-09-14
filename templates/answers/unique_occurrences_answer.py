
from typing import List

def unique_occurrences(nums: List[int]) -> bool:
    # Create a dictionary to count occurrences of each number
    num_counts_dic = {}

    for num in nums:
        # Increment count if number already exists, else set to 1
        if num in num_counts_dic:
            num_counts_dic[num] += 1
        else:
            num_counts_dic[num] = 1

    # Create a set of the occurrence counts to get unique values
    unique_occurrence_set = set(num_counts_dic.values())
    # If the number of unique counts equals the number of numbers, all counts are unique
    return len(unique_occurrence_set) == len(num_counts_dic.values())

if __name__ == '__main__':
    nums = [1,2,2,1,1,3]
    expected = True
    result = unique_occurrences(nums)
    print(f"nums={nums} expected={expected} result={result}")
    assert result == expected, f"Expected {expected}, but got {result}"

    nums = [1, 2]
    expected = False
    result = unique_occurrences(nums)
    print(f"nums={nums} expected={expected} result={result}")
    assert result == expected, f"Expected {expected}, but got {result}"

    nums = [-3,0,1,-3,1,1,1,-3,10,0]
    expected = True
    result = unique_occurrences(nums)
    print(f"nums={nums} expected={expected} result={result}")
    assert result == expected, f"Expected {expected}, but got {result}"


