
from typing import List

def triplet_sum(nums: List[int]) -> List[List[int]]:
    triplets = []
    nums.sort()

    for i in range(len(nums)):

        # early break if positive num since it's sorted and all positive can't sum to 0
        if(nums[i] > 0):
            break

        # continue to next if current is same as previous to avoid dupes
        if(i > 0 and nums[i] == nums[i - 1]):
            continue

        pairs = pairs_sum_sorted_all_pairs(nums, i + 1, -nums[i])

        for pair in pairs:
            triplets.append([nums[i]] + pair)

    return triplets

def pairs_sum_sorted_all_pairs(nums: List[int], start: int, target: int) -> List[List[int]]:
    pairs = []
    left, right = start, len(nums) - 1

    while left < right:
        sum = nums[left] + nums[right]

        if(sum == target):
            pairs.append([nums[left], nums[right]])
            left += 1
            #find next left value that is different than previous
            while left < right and nums[left] == nums[left - 1]:
                left += 1
        elif(sum < target):
            left += 1
        else:
            right -= 1

    return pairs

if __name__ == '__main__':
    nums = [0,-1,2,-3,1]
    expected = [[-3,1,2],[-1,0,1]]
    result = []

    result = triplet_sum(nums)

    print(result)
    assert result == expected, f"Expected {expected}, but got {result}"
